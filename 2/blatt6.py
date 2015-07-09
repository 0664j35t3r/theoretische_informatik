  ###################### Erster Teil #########################
  while Z_i not Z_m                                       # 1. big loop
    # ROW1 creates guess and check
    while iter1 != square and iter1 != '#'                # 1.1 inner loop
      helpband[Z_i][1] = '0'
      # create TM for each element in row to simulate all outcomes
      new TM[Z_i][iter1] # consits of rootband and helpband
      iter1++

    # ROW2 goes back to the left on all new Turing machines
    while iter1 != square and iter1 != '#'                # 1.2 inner loop
      iter1--

    # ROW3 checks if row is empty, 
    # if not confirm to the rules of solitaire and deletes this TM
    while iter1 == '-'                                    # 1.3 inner loop
      if iter1 == '1' or iter1 == '0' then
      change_state_to ROW1
      iter1++

    if helpband_k[iter1 - 1] != '1' then 
      delete TM[Z_i]
  Z_i++

  ###################### Zeiter Teil #########################
  # COL1 copy                                             # 2 big loop
  while rootband[iter1] != '#' 
    helpband[iter2] = rootband[iter1]
    iter1--
    iter2--

  goto (rootband.end() and helpband.end())

  # compares rootband and helpband Z_m
  #ROW1 and ROW2                                          
    for Z_i = Z_m-1 downto Z_1                            # 3 big loop
      for iter1 = n downto 1                              # 3.1 inner loop
        if helpband[iter1] == '-' and rootband[Z_i][iter1] == '0' then 
          helpband[iter1] = '0'

        if helpband[iter1] == '-' and rootband[Z_i][iter1] == '1' then 
          helpband[iter1] = '1'

        if helpband[iter1] == '1' and rootband[Z_i][iter1] == '0' then 
          delete TM[Z_i]

        if helpband[iter1] == '0' and rootband[Z_i][iter1] == '1' then 
          delete TM[Z_i]