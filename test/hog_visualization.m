(* Mathematica Script to Visualize HOG overlayed on image *)

img = (* Place Image Here *);
dims = ImageDimensions[img];
dirs = ImageData[GradientOrientationFilter[img, 5]];
magnitudes = ImageData[GradientFilter[img, 5]];
orientations = 
    MapThread[#1 {-Sin[#2], Cos[#2]} &, {magnitudes, dirs}, 2];
Show[img, 
  ListVectorPlot[
    MapIndexed[{{#2[[2]], dims[[2]] - #2[[1]]}, #1} &, 
      orientations, {2}], VectorColorFunction -> (Yellow &)]]