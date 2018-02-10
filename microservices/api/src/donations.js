var express = require('express');
var router = express.Router();

router.route("/").get(function (req, res) {
  res.send([{
    id: 1,
    amount: 2000,
    description: "loved to help ya",
    date: "2018-02-10T12:18:46.736Z",
    paid_to: 1
  }, {
    id: 2,
    amount: 1000,
    description: "keep going",
    date: "2018-02-08T12:18:46.736Z",
    paid_to: 1
  }, {
    id: 3,
    amount: 5000,
    description: "awesome",
    date: "2018-01-08T12:18:46.736Z",
    paid_to: 2
  }])
})

module.exports = router;
