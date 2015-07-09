# iter1 ... Iterator for tape 1
# iter2 ... Iterator for tape 2

# START GUESS and CHECK

counter = 1
while A(v_i) not A(v_n)      # Oracle, Create 2^n TM'S
  new TM[A(v_i)][counter]
    do COPY to tape2
  new TM[A(v_i)][counter]
    do JUMP
  counter++

# COPY bin(k) to tape 2
duplicate( bin(k), bin_2(k), tape1.end() )

# CHECK LENGTH
if |A(v_i) on tape2| != bin_2(k) then
  delete this.TM

# DELETE RIGHT
loop = l_g + l_k
while loop < l_g + 2 * l_k
  tape1[loop] = blank
  loop++

# COPY LEFT VERTEX
amount = bin(k)

# CHECK IF 0
while bin(k) > 0
  # DO NEXT VERTEX
  if |tape2[A(v_1)]| > 0 then
    cut( tape2[A(v_1)][1], tape1.end() )
    vertex = tape1[last_bin]
  else
    delete this.TM

  # CHECK VERTEX
  i = 2
  isInAll = True
  while i <= amount
    loop = 1
    isThere = False
    while loop <= |tape2[A(v_i)]|
      if vertex == tape2[A(v_i)][loop] then
        isThere = True
        break
      loop++

    if isThere == False then
      isInAll = False
      break

    # TAKE NEXT VERTEX
    i++

  # DECREMENT COUNTER
  if isInAll == True
    bin(k)--

# EXIT
