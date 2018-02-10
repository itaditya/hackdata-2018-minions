var express = require('express');
var router = express.Router();

router.route("/").get(function (req, res) {
  res.send([{
    id: 1,
    name: "Woman Who Startup",
    description: "We are a community to help women"
  }, {
    id: 2,
    name: "Happy Claps",
    description: "Make some happy claps"
  }, {
    id: 3,
    name: "Smoky Cakes",
    description: "Best cakes you ever taste"
  }])
})

module.exports = router;
