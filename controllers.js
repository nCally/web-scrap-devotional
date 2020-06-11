
let devotional = require("./devotional-model");

module.exports = {

  // Controller to return todays every day with Jesus
  async get_today(req, res) {
    //
    let latest = await devotional.findOne({
      limit: 1,
      order: [['createdAt', 'DESC']]
    })
    latest = latest.get({ plain: true });
    res.status(200).json({
      data: latest
    })
  },

  // Controller to save what is gotten from the web scrap
  async add_today(req, res) {
    //
    let saved = await devotional.create(req.body);
    if (saved) {
      res.sendStatus(200)
    } else {
      res.sendStatus(200);
    }

  }
}
