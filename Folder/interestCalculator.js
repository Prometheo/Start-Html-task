data = [{'principal':2500, 'time':1.8}, {'principal':1000, 'time':5},{'principal':3000, 'time':1}, {'principal':2000, 'time':3}]

function interestCalculator(ray) {
  let rate;
  let interest;
  let interestData = [...ray];
  for (let ob of interestData) {
    if (ob['principal'] >= 2500 && (ob['time'] > 1 && ob['time'] <= 3) ) {
      rate = 3;
      ob['rate'] = rate;
    } else if (ob['principal'] >= 2500 && ob['time'] >= 3) {
      rate = 4;
      ob['rate'] = rate;
    } else if (ob['principal'] < 2500 || ob['time'] <= 1) {
      rate = 2;
      ob['rate'] = rate;
    } else {
      rate = 1;
      ob['rate'] = rate;
    } 
    interest = (ob['principal']*ob['time']*ob['rate'])/100;
    ob['interest'] = interest
  }
  console.log(interestData);
  return interestData
}

interestCalculator(data);
