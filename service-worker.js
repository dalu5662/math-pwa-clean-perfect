// service-worker.js
self.addEventListener('install', function(event) {
  console.log('[Service Worker] 安装成功');
});

self.addEventListener('fetch', function(event) {
  // 暂时不处理任何网络请求，仅作注册测试
  // event.respondWith(fetch(event.request));
});