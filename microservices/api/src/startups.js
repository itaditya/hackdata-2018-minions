var express = require('express');
var router = express.Router();

router.route("/").get(function (req, res) {
  res.send([{
    id: 1,
    name: "Woman Who Startup",
    description: "We are a company hell-bound to help women"
  }, {
    id: 2,
    name: "Gen Startup",
    description: "You are the Youth, you are the change, help us help you"
  }, {
    id: 3,
    name: "GoSoccer",
    description: "Support your Favorite Football Club with ease"
  }])
})

module.exports = router;
