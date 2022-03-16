const fs = require('fs');
const { parse } = require('json2csv');



// console.log(path.join(__dirname, 'recipeData.json'));

const data = JSON.parse(fs.readFileSync('./data/recipesData.json', 'utf8'));

const fields = Object.keys(data[0]);
const opts = { fields };

try {
    const csv = parse(data, opts);
    // console.log(csv);
    fs.writeFileSync('./data/recipesData.csv', csv, 'utf8');
  } catch (err) {
    console.error(err);
  }

// Parser.Transform()
// console.log(data)