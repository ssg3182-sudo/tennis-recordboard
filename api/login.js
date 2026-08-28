// Vercel Serverless Function — POST /api/login
// PIN을 검증하고, 맞으면 Firebase 커스텀 인증 토큰을 발급합니다.
// 이 파일은 서버에서만 실행되므로 TENNIS_PIN, FIREBASE_* 값이 브라우저에 노출되지 않습니다.

const admin = require('firebase-admin');

let app;
function getAdminApp() {
  if (app) return app;
  const projectId = (process.env.FIREBASE_PROJECT_ID || '').trim();
  const clientEmail = (process.env.FIREBASE_CLIENT_EMAIL || '').trim();
  let privateKey = (process.env.FIREBASE_PRIVATE_KEY || '').trim();
  // 흔한 실수 방지: Value 칸에 앞뒤 큰따옴표까지 같이 붙여넣은 경우 제거
  if (privateKey.startsWith('"') && privateKey.endsWith('"')) {
    privateKey = privateKey.slice(1, -1);
  }
  // "\n" 이라는 두 글자(백슬래시+n)로 저장된 줄바꿈을 실제 줄바꿈으로 변환
  privateKey = privateKey.replace(/\\n/g, '\n').trim();
  if (
    !projectId ||
    !clientEmail ||
    !privateKey ||
    !privateKey.includes('BEGIN PRIVATE KEY') ||
    !privateKey.includes('END PRIVATE KEY')
  ) {
    throw new Error(
      'Firebase Admin 환경변수가 없습니다 (FIREBASE_PROJECT_ID / FIREBASE_CLIENT_EMAIL / FIREBASE_PRIVATE_KEY). Vercel 프로젝트 설정 > Environment Variables에서 추가해주세요.'
    );
  }
  app = admin.initializeApp({
    credential: admin.credential.cert({ projectId, clientEmail, privateKey }),
  });
  return app;
}

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    res.status(405).json({ error: 'POST 요청만 허용됩니다.' });
    return;
  }

  try {
    const body = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
    const pin = String(body.pin || '').trim();
    const expected = process.env.TENNIS_PIN;

    if (!expected) {
      res.status(500).json({ error: '서버에 TENNIS_PIN 환경변수가 설정되지 않았어요.' });
      return;
    }

    if (!pin || pin !== expected) {
      await new Promise((r) => setTimeout(r, 400));
      res.status(401).json({ error: 'PIN이 올바르지 않아요.' });
      return;
    }

    getAdminApp();
    const token = await admin.auth().createCustomToken('tennis-editor');
    res.status(200).json({ token });
  } catch (err) {
    console.error('[api/login] error:', err);
    res.status(500).json({ error: err.message || '로그인 처리 중 오류가 발생했어요.' });
  }
};
