var express = require('express');
var router = express.Router();

router.route("/").get(function(req, res) {
  res.send([{
    id: 1,
    change: { amount: 11528, sign: "-" },
    date: "2018-02-11T12:18:46.736Z"
  }, {
    id: 2,
    change: { amount: 50603, sign: "+" },
    date: "2018-02-12T12:18:46.736Z"
  }, {
    id: 3,
    change: { amount: 68152, sign: "+" },
    date: "2018-01-13T12:18:46.736Z"
  }, {
    id: 4,
    change: { amount: 77660, sign: "-" },
    date: "2018-01-14T12:18:46.736Z"
  }, {
    id: 5,
    change: { amount: 129850, sign: "+" },
    date: "2018-01-15T12:18:46.736Z"
  }])
})

module.exports = router;
