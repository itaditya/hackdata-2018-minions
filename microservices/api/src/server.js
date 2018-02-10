var express = require('express');
var app = express();
var request = require('request');
var router = express.Router();
var morgan = require('morgan');
var bodyParser = require('body-parser');
require('request-debug')(request);

var hasuraExamplesRouter = require('./hasuraExamples');
var startupsRouter = require('./startups');
var donationsRouter = require('./donations');
var predictionsRouter = require('./predictions');

var server = require('http').Server(app);

router.use(morgan('dev'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));

app.use('/', hasuraExamplesRouter);
app.use('/api/startups', startupsRouter);
app.use('/api/donations', donationsRouter);
app.use('/api/predictions', predictionsRouter);

app.listen(8080, function () {
  console.log('Example app listening on port 8080!');
});
