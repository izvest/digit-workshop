const autoprefixer = require('autoprefixer');

exports.autoprefix = (production) =>  ({
  loader: 'postcss-loader',
  options: {
    sourceMap: !production,
    plugins: () => [
      require('postcss-flexbugs-fixes'),
      autoprefixer({ browsers: '> 1%' }),
    ],
  },
});

exports.cssLoader = (production) => ({
  loader: 'css-loader',
  options: {
    sourceMap: !production,
  },
});

exports.sassLoader = (production) => ({
  loader: 'sass-loader',
  options: {
    sourceMap: !production,
  },
});
