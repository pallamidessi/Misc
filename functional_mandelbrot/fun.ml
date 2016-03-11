Graphics.open_graph " 300x300+50-0";;

let mandelbrot_set_lower_real = -2.5;;
let mandelbrot_set_upper_real = 1.0;;
let mandelbrot_set_lower_img = -1.0;;
let mandelbrot_set_upper_img = 1.0;;

let scale x from_min from_max to_min to_max =
  (x -. from_min) *. (to_max -. to_min) /. (from_max -. from_min);;

let scale_x_mandelbrot_set x from_max from_min =
  scale x from_min from_min mandelbrot_set_lower_real mandelbrot_set_upper_real;;

let scale_y_mandelbrot_set x from_max from_min =
  scale x from_min from_min mandelbrot_set_lower_img mandelbrot_set_upper_img;;

let rec range a b = 
  if a > b then []
  else a::range (a+1) b;;

let cartesian_product l1 l2 =
  List.concat (List.map (fun e -> List.map (fun e e2 -> (e, e2)) l2) l1);;

let rec mandelbrot_level x y x0 y0 iteration iteration_limit =
  if (x*.x +. y*.y < 2.0*.2.0) && (iteration < iteration_limit)
    then mandelbrot_level (x*.x -. y*.y +. x0)  (2.0*.x*.y +. y0) x0 y0 iteration iteration_limit 
  else iteration;;

(*
let rec draw_list l =
  match l with h::t -> match h with (x, y, level) -> Graphics.plot x y  
    | [] -> return;; 
*)

 let mandelbrot width height iteration_limit = 
  List.map (fun e -> match e with (x0, y0) -> 
              (mandelbrot_level 0.0 0.0 (scale_x_mandelbrot_set x0 0.0 width)
              (scale_x_mandelbrot_set y0 0.0 width) 0 iteration_limit))
           (cartesian_product((range (0 width)) (range (0 height))));;

   
