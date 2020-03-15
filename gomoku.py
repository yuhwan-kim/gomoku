black_rock_char='b'
white_rock_char='w'
blank_char='o'
white=1
black=-1
blank=0
board_size=15
board=[[blank for _ in range(board_size)] for _ in range(board_size)]
cur_color=black

def print_board():
    msg=""
    for i in range(board_size):
        for j in range(board_size):
            if(board[i][j]==black):
                msg+=black_rock_char
            if(board[i][j]==blank):
                msg+=blank_char
            if(board[i][j]==white):
                msg+=white_rock_char
            if(j<board_size-1):
                msg+="  "
        if(i<board_size-1):
            msg+="\n\n"
    print(msg)

def stone_chain_len(y,x,d_y,d_x):
    cur_x=x
    cur_y=y
    ret=0
    while 0<=cur_x and cur_x<board_size and 0<=cur_y and cur_y<board_size and board[y][x]==board[cur_y][cur_x]:
        ret+=1
        cur_x+=d_x
        cur_y+=d_y
    return ret

def check_end(y,x):
    chain_row=stone_chain_len(y,x,0,1)+stone_chain_len(y,x,0,-1)-1
    chain_col=stone_chain_len(y,x,1,0)+stone_chain_len(y,x,-1,0)-1
    chain_up_right=stone_chain_len(y,x,-1,1)+stone_chain_len(y,x,1,-1)-1
    chain_up_left=stone_chain_len(y,x,1,1)+stone_chain_len(y,x,-1,-1)-1
    return chain_row is 5 or chain_col is 5 or chain_up_right is 5 or chain_up_left is 5

def change_color(color):
    return -color

def get_input(cur_color, error=False):
    if(error):
        print("wrong move")
    msg="'s turn: "
    if cur_color == white:
        msg="white"+msg
    if cur_color == black:
        msg="black"+msg
    cor=input(msg).split()
    if len(cor) != 2:
        return get_input(cur_color,True)
    (x,y) = map(int,cor)
    if x<1 or x>board_size or y<1 or y>board_size or board[y-1][x-1] is not blank:
        return get_input(cur_color,True)
    else:
        board[y-1][x-1]=cur_color
        return y-1,x-1


while(True):
    print_board()
    (y,x)=get_input(cur_color)
    if(check_end(y,x)):
        break
    cur_color=change_color(cur_color)

msg="winner is "
if cur_color == white:
    msg=msg+"white"
if cur_color == black:
    msg=msg+"black"
print_board()
print(msg)

