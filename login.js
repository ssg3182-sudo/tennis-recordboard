// Vercel Serverless Function — POST /api/login
// PIN을 검증하고, 맞으면 Firebase 커스텀 인증 토큰을 발급합니다.
// 이 파일은 서버에서만 실행되므로 TENNIS_PIN, FIREBASE_* 값이 브라우저에 노출되지 않습니다.

const admin = require('firebase-admin');

let app;
function getAdminApp() {
  if (app) return app;
  const projectId = process.env.FIREBASE_PROJECT_ID;
  const clientEmail = process.env.FIREBASE_CLIENT_EMAIL;
  const privateKey = (process.env.FIREBASE_PRIVATE_KEY || '').replace(/\\n/g, '\n');
  if (!projectId || !clientEmail || !privateKey) {
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
      // 무차별 대입 시도를 조금이라도 늦추기 위한 지연
      await new Promise((r) => setTimeout(r, 400));
      res.status(401).json({ error: 'PIN이 올바르지 않아요.' });
      return;
    }

    getAdminApp();
    // 고정된 하나의 "editor" 계정으로 로그인시킵니다 (PIN을 아는 사람은 모두 같은 편집 권한을 가져요).
    const token = await admin.auth().createCustomToken('tennis-editor');
    res.status(200).json({ token });
  } catch (err) {
    console.error('[api/login] error:', err);
    res.status(500).json({ error: err.message || '로그인 처리 중 오류가 발생했어요.' });
  }
};
