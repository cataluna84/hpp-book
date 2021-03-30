Length of x: 1000
Total elements: 1000000
Filename: julia1_memoryprofiler.py

Line #    Mem usage    Increment   Line Contents
================================================
     9  115.289 MiB  115.289 MiB   @profile
    10                             def calculate_z_serial_purepython(maxiter, zs, cs):
    11                                 """Calculate output list using Julia update rule"""
    12  122.812 MiB    7.523 MiB       output = [0] * len(zs)
    13  123.348 MiB    0.000 MiB       for i in range(len(zs)):
    14  123.348 MiB    0.000 MiB           n = 0
    15  123.348 MiB    0.000 MiB           z = zs[i]
    16  123.348 MiB    0.000 MiB           c = cs[i]
    17  123.348 MiB    0.000 MiB           while n < maxiter and abs(z) < 2:
    18  123.348 MiB    0.258 MiB               z = z * z + c
    19  123.348 MiB    0.000 MiB               n += 1
    20  123.348 MiB    0.000 MiB           output[i] = n
    21                                 return output


Filename: julia1_memoryprofiler.py

Line #    Mem usage    Increment   Line Contents
================================================
    24   37.852 MiB   37.852 MiB   @profile
    25                             def calc_pure_python(draw_output, desired_width, max_iterations):
    26                                 """Create a list of complex co-ordinates (zs) and complex parameters (cs), build Julia set and display"""
    27   37.852 MiB    0.000 MiB       x_step = (float(x2 - x1) / float(desired_width))
    28   37.852 MiB    0.000 MiB       y_step = (float(y1 - y2) / float(desired_width))
    29   37.852 MiB    0.000 MiB       x = []
    30   37.852 MiB    0.000 MiB       y = []
    31   37.852 MiB    0.000 MiB       ycoord = y2
    32   37.934 MiB    0.082 MiB       while ycoord > y1:
    33   37.934 MiB    0.000 MiB           y.append(ycoord)
    34   37.934 MiB    0.000 MiB           ycoord += y_step
    35   37.934 MiB    0.000 MiB       xcoord = x1
    36   37.934 MiB    0.000 MiB       while xcoord < x2:
    37   37.934 MiB    0.000 MiB           x.append(xcoord)
    38   37.934 MiB    0.000 MiB           xcoord += x_step
    39                                 # set width and height to the generated pixel counts, rather than the
    40                                 # pre-rounding desired width and height
    41                                 # build a list of co-ordinates and the initial condition for each cell.
    42                                 # Note that our initial condition is a constant and could easily be removed,
    43                                 # we use it to simulate a real-world scenario with several inputs to our
    44                                 # function
    45   37.934 MiB    0.000 MiB       zs = []
    46   37.934 MiB    0.000 MiB       cs = []
    47  115.289 MiB    0.000 MiB       for ycoord in y:
    48  115.289 MiB    0.000 MiB           for xcoord in x:
    49  115.289 MiB    0.512 MiB               zs.append(complex(xcoord, ycoord))
    50  115.289 MiB    0.258 MiB               cs.append(complex(c_real, c_imag))
    51                             
    52  115.289 MiB    0.000 MiB       print("Length of x:", len(x))
    53  115.289 MiB    0.000 MiB       print("Total elements:", len(zs))
    54  115.289 MiB    0.000 MiB       start_time = time.time()
    55                                 output = calculate_z_serial_purepython(max_iterations, zs, cs)
    56                                 end_time = time.time()
    57                                 secs = end_time - start_time
    58                                 print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")
    59                             
    60                                 # this sum is expected for 1000^2 grid with 300 iterations
    61                                 assert sum(output) == 33219980


