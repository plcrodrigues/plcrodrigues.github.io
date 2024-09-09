var data  = null;
var graph = null;

// Called when the Visualization API is loaded.
function drawVisualization(divname, filename) {

  d3.text(filename, function(error, data_){
    
    points = d3.csvParseRows(data_, function(d, i) {
      return {
        x: +d[0], // x-coordinate in float
        y: +d[1], // y-coordinate in float      
        z: +d[2], // z-coordinate in float
        c: d[3],  // color for the point in HEX
      };
    });

    // create the data table.
    data = new vis.DataSet();   

    // create the animation data
    var imax = points.length;
    for (var i = 0; i < imax; i++) {
      var x = points[i].x;
      var y = points[i].y;
      var z = points[i].z;
      var style = points[i].c;

      data.add({x:x,y:y,z:z,style:style});

    }

    // specify options
    var options = {
      dotSizeRatio: 0.015,
      width:  '700px',
      height: '700px',
      style: 'dot-color',
      showPerspective: true,
      showGrid: false,
      keepAspectRatio: true,
      verticalRatio: 1.0,
      showLegend: false,
      legendLabel: 'distance',
      onclick: onclick,
      cameraPosition: {
        horizontal: -0.35,
        vertical: 0.22,
        distance: 2.0
      },
      xCenter: '55%',
      yCenter: '35%',
    };

    // create our graph
    var container = document.getElementById(divname);
    graph = new vis.Graph3d(container, data, options);

    });

}