def if_overlap(line1,line2):
  #Checks if the both lines overlap at anypoint, It returns either True(The line overlaps at a point) or False(They dont overlap)
  
  def checkboundary(x, y):
  #This help function checks if any of the points in a line exist with the boundary of the other line
    return min(y) <= x <= max(y)

  return checkboundary(line1[0], line2) or checkboundary(line1[1], line2)




