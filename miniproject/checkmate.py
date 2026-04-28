def checkmate(board_str):
    # 1.แปลง string เป็น list 2D (ตาราง)
    board = [list(row) for row in board_str.strip().split('\n')]
    size = len(board)
    
    # 2. หาตำแหน่งของ King (K)
    king_pos = None
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
    
    if not king_pos:
        return # ถ้าไม่มีKingไม่ต้องทำไรอยู่ซื่อๆ

    kr, kc = king_pos

    # 3. กำหนดทิศทางการเดินของหมาก
    directions = {
        'P': [(-1, -1, 'single'), (-1, 1, 'single')], # Pawn รุกเฉียงขึ้น
        'R': [(0, 1, 'infinite'), (0, -1, 'infinite'), (1, 0, 'infinite'), (-1, 0, 'infinite')], # Rook บนล่างซ้ายขวา
        'B': [(1, 1, 'infinite'), (1, -1, 'infinite'), (-1, 1, 'infinite'), (-1, -1, 'infinite')], # Bishop เฉียง 4 ทิศ
        'Q': [(0, 1, 'infinite'), (0, -1, 'infinite'), (1, 0, 'infinite'), (-1, 0, 'infinite'),
              (1, 1, 'infinite'), (1, -1, 'infinite'), (-1, 1, 'infinite'), (-1, -1, 'infinite')] # Queen ทุกทิศ
    }

    # 4. ดูศัตรูรอบตัว King
    for piece, moves in directions.items():
        for dr, dc, mode in moves:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                found = board[r][c]
                if found != '.':
                    if found == piece or (found == 'Q' and piece in 'RB'):
                        print("Success")
                        return
                    break # หยุดนะจ็ะคนดีของพี่โดนหมากขวางทาง
                if mode == 'single':
                    break
                r, c = r + dr, c + dc
                
    print("Fail")