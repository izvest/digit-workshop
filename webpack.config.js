const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const webpackParts = require('./webpack-parts');

const production = process.env.NODE_ENV === 'production';

module.exports = {
  entry: './digit_project/static_src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'digit_project/static'),
  },
  devtool: production ? false : 'source-map',
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          webpackParts.cssLoader(production),
          webpackParts.autoprefix(production),
          webpackParts.sassLoader(production),
        ],
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          'file-loader',
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[name]-chunk.css',
    }),
  ]
};
