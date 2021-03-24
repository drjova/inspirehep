const proxy = require('http-proxy-middleware');

const localProxy = proxy({
  target: 'https://inspirebeta.net',
  secure: false,
  changeOrigin: true,
});

module.exports = (app) => {
  app.use('/api', localProxy);
};
