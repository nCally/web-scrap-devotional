
const { DataTypes, Model } = require("sequelize");
const db = require("./db");

class Devotional extends Model { }

Devotional.init(
  {
    id: {
      type: DataTypes.UUID,
      primaryKey: true,
      defaultValue: DataTypes.UUIDV4
    },
    day: {
      type: DataTypes.TEXT,
      allowNull: false
    },
    main: DataTypes.TEXT,
    focus: DataTypes.TEXT,
    topic: DataTypes.TEXT,
    reference: DataTypes.TEXT,
    reading: DataTypes.TEXT,
    prayer: DataTypes.TEXT,
  },
  {
    sequelize: db
  }
)

module.exports = Devotional;