function drawScatter(container, data) {
  var colorLayout = data.colorLayout,
      markSize = data.markSize;

  // Last color is the target
  var colorSets = [
      ['rgb(120,106,24)','rgb(131,71,80)','rgb(23,73,95)','rgb(0,68,43)','rgb(98,63,117)'],
      ['rgb(131,71,80)','rgb(120,106,24)','rgb(0,68,43)','rgb(23,73,95)','rgb(98,63,117)'],
      ['rgb(23,73,95)','rgb(0,68,43)','rgb(120,106,24)','rgb(131,71,80)','rgb(98,63,117)'],
      ['rgb(0,68,43)','rgb(23,73,95)','rgb(131,71,80)','rgb(120,106,24)','rgb(98,63,117)'],
  ];
  var colorSet = colorSets[Math.floor(Math.random() * colorSets.length)];

  var margin = {'bottom': 10, 'left': 10, 'right': 10, 'top': 10},
      chartH = 800,
      chartW = 800,
      svgH = chartH + margin.top + margin.bottom,
      svgW = chartW + margin.left + margin.right;

  var svg = container.append('svg')
          .attr('height', svgH)
          .attr('id', 'plot')
          .attr('width', svgW)
          .style('background', '#000000')
          .style('display', 'inline-block')
        .append("g")
          .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
          .style('border', '1px solid #333');

  var x = d3.scale.linear()
    .range([0, chartW]);

  var y = d3.scale.linear()
      .range([chartH, 0]);

  var color = d3.scale.category10();

  var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom");

  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");

  xExtent = d3.extent(data.pts, function(d) { return parseFloat(d.x); });
  yExtent = d3.extent(data.pts, function(d) { return parseFloat(d.y); });
  x.domain(xExtent).nice();
  y.domain(yExtent).nice();

  svg.append('line')
    .attr("x1", chartW/2)
    .attr("y1", 0)
    .attr("x2", chartW/2)
    .attr("y2", chartH)
    .style("stroke", "#333");
  svg.append('line')
    .attr("x1", 0)
    .attr("y1", chartH/2)
    .attr("x2", chartW)
    .attr("y2", chartH/2)
    .style("stroke", "#333");

  svg.selectAll(".dot")
      .data(data.pts)
    .enter().append("rect")
      .attr("class", "dot")
      .attr("width", markSize)
      .attr('height', markSize)
      .attr("x", function(d) { return x(d.x); })
      .attr("y", function(d) { return y(d.y)  - markSize/2; })
      .style("fill", function(d) {
        if (colorLayout == 'grouped') {
          return colorSet[d.cluster - 1];
        } else {
          return colorSet[d.randColor - 1];
        }
      });//color(d.cluster); });
}