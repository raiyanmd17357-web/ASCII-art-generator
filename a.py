def generate_ascii_art():
    height = 38
    width = 80

    for row in range(height):
        for column in range(width):
            char = " "

            # Row 1
            if row == 1:
                if column == 31:
                    char = ":"
                elif column == 32:
                    char = "%"
                elif column == 33:
                    char = ":"
                elif column == 39:
                    char = "%"
                elif column == 40:
                    char = "@"
                elif column == 41:
                    char = "+"
                elif column == 46:
                    char = ":"

            # Row 2
            elif row == 2:
                if column == 32:
                    char = "+"
                elif column == 33:
                    char = "#"
                elif column == 34:
                    char = "+"
                elif column == 35:
                    char = "@"
                elif column == 36:
                    char = "#"
                elif column == 37:
                    char = "%"
                elif 38 <= column <= 40:
                    char = "@"
                elif column == 41:
                    char = "#"
                elif column == 42:
                    char = "*"
                elif column == 43:
                    char = "%"
                elif column == 44:
                    char = "*"
                elif column == 45:
                    char = "#"
                elif column == 46:
                    char = "@"
                elif column == 47:
                    char = ":"
                elif column == 48:
                    char = ":"

            # Row 3
            elif row == 3:
                if column == 24:
                    char = ":"
                elif column == 26:
                    char = ":"
                elif column == 28:
                    char = "*"
                elif column == 29:
                    char = "#"
                elif column == 30:
                    char = "#"
                elif column == 31:
                    char = "%"
                elif column == 32:
                    char = "%"
                elif 33 <= column <= 53:
                    char = "@"
                elif column == 54:
                    char = "%"
                elif column == 55:
                    char = "+"
                elif column == 56:
                    char = "="
                elif column == 57:
                    char = "="
                elif column == 58:
                    char = ":"
            elif row == 4:
                if column == 23:
                    char = "#"
                elif column == 24:
                    char = "%"
                elif column == 25:
                    char = "="
                elif 26 <= column <= 52:
                    char = "@"
                elif column == 53:
                    char = "*"
            elif row == 5:
                if column == 18:
                    char = "="
                elif column == 19:
                    char = "-"
                elif column == 20:
                    char = ":"
                elif column == 21:
                    char = "+"
                elif 22 <= column <= 53:
                    char = "@"
                elif column == 54:
                    char = "+"
                elif column == 55:
                    char = "-"
                elif column == 56:
                    char = "-"
            elif row == 6:
                if column == 17:
                    char = "+"
                elif 18 <= column <= 57:
                    char = "@"
                elif column == 58:
                    char = "+"
                elif column == 59:
                    char = ":"
                elif column == 60:
                    char = ":"
                elif column == 61:
                    char = "-"
            elif row == 7:
                if column == 15:
                    char = "+"
                elif column == 16:
                    char = "#"
                elif column == 17:
                    char = "+"
                elif 18 <= column <= 59:
                    char = "@"
                elif column == 60:
                    char = "="
            elif row == 8:
                if column == 15:
                    char = "#"
                elif 16 <= column <= 60:
                    char = "@"
                elif column == 61:
                    char = "+"
            elif row == 9:
                if column == 14:
                    char = "-"
                elif column == 15:
                    char = "%"
                elif 16 <= column <= 60:
                    char = "@"
                elif column == 61:
                    char = "*"
        
            elif row == 10:
                if column == 11:
                    char = "-"
                elif column == 12:
                    char = "-"
                elif column == 13:
                    char = ":"
                elif column == 14:
                    char = "%"
                elif 15 <= column <= 61:
                    char = "@"
                elif column == 62:
                    char = "="
            elif row == 11:
                if column == 13:
                    char = "="
                elif 14 <= column <= 25:
                    char = "@"
                elif column == 26:
                    char = "%"
                elif column == 27:
                    char = ":"
                elif column == 28:
                    char = "."
                elif column == 29:
                    char = "."
                elif column == 30:
                    char = ":"
                elif column == 48:
                    char = "="
                elif 49 <= column <= 60:
                    char = "@"
                elif column == 61:
                    char = "*"
            elif row == 12:
                if column == 13:
                    char = "+"
                elif 14 <= column <= 24:
                    char = "@"
                elif column == 25:
                    char = "="
                elif column == 49:
                    char = ":"
                elif 50 <= column <= 61:
                    char = "@"
                elif column == 62:
                    char = "*"
            elif row == 13:
                if column == 12:
                    char = "="
                elif 13 <= column <= 23:
                    char = "@"
                elif column == 24:
                    char = "#"
                elif column ==  50:
                    char = "%"
                elif 51 <= column <= 61:
                    char = "@"
                elif column == 62:
                    char = "%"
                elif column == 63:
                    char = "#"
            elif row == 14:
                if column == 11:
                    char = ":"
                elif column == 12:
                    char = ":"
                elif column == 13:
                    char = "+"
                elif 14 <= column <= 23:
                    char = "@"
                elif column == 24:
                    char = "*"
                elif column == 50:
                    char = "%"
                elif 51 <= column <= 60:
                    char = "@"
                elif column == 61:
                    char = "%"
                elif column == 62:
                    char = "+"
                elif column == 63:
                    char = "+"
            elif row == 15:
                if column == 12:
                    char = ":"
                elif column == 13:
                    char = "%"
                elif 14 <= column <= 23:
                    char = "@"
                elif column == 24:
                    char = "*"
                elif column == 43:
                    char = ":"
                elif column == 46:
                    char = ":"
                elif column == 50:
                    char = ":"
                elif column == 51:
                    char  = "*"
                elif 52 <= column <= 60:
                    char = "@"
                elif column == 61:
                    char = "#"
                elif column == 62:
                    char = "-"
                elif column == 63:
                    char = ":"
            elif row == 16:
                if column == 14:
                    char = "#"
                elif 15 <= column <= 23:
                    char = "@"
                elif 24 <= column <= 27:
                    char = "."
                elif column == 28:
                    char = ":"
                elif column == 29:
                    char = "="
                elif column == 30:
                    char = "-"
                elif column == 31:
                    char = ":"
                elif column == 32:
                    char = "="
                elif column == 33:
                    char = "*"
                elif column == 34:
                    char = "#"
                elif column == 35:
                    char = "*"
                elif 36 <= column <= 38:
                    char = "-"
                elif column == 39:
                    char = "="
                elif column == 40:
                    char = "*"
                elif column == 41:
                    char = "@"
                elif column == 42:
                    char = "@"
                elif 43 <= column <= 45:
                    char = "*"
                elif column == 46:
                    char = "+"
                elif column == 47:
                    char = "+"
                elif column == 48:
                    char = "*"
                elif column == 49:
                    char = "="
                elif 50 <= column <= 51:
                    char = "."
                elif column == 52:
                    char = "#"
                elif 53 <= column <= 61:
                    char = "@"
                elif column == 62:
                    char = "-"
            elif row == 17:
                if column == 14:
                    char = "#"
                elif 15 <= column <= 21:
                    char = "@"
                elif column == 22:
                    char = "#"
                elif column == 23:
                    char = "."
                elif column == 24:
                    char = ":"
                elif column == 25:
                    char = "*"
                elif 26 <= column <= 35:
                    char = "@"
                elif column == 36:
                    char = "*"
                elif column == 37:
                    char = "#"
                elif column == 38:
                    char = "#"
                elif column == 39:
                    char = "*"
                elif column == 40:
                    char = "#"
                elif 41 <= column <= 50:
                    char = "@"
                elif column == 51:
                    char = "%"
                elif column == 52:
                    char = "="
                elif 53 <= column <= 59:
                    char = "@"
                elif column == 60:
                    char = "#"
                elif column == 61:
                    char = ":"
            elif row == 18:
                if column == 14:
                    char = "%"
                elif column == 15:
                    char = "%"
                elif 16 <= column <= 21:
                    char = "@"
                elif column == 22:
                    char = "-"
                elif column == 23:
                    char = "."
                elif column == 24:
                    char = "%"
                elif 25 <= column <= 35:
                    char = "@"
                elif column == 36:
                    char = "+"
                elif column == 37:
                    char = "*"
                elif column == 38:
                    char = "="
                elif column == 39:
                    char = "@"
                elif column == 40:
                    char = "*"
                elif 41 <= column <= 50:
                    char = "@"
                elif column == 51:
                    char = "%"
                elif column == 52:
                    char = "."
                elif column == 53:
                    char = "#"
                elif column == 54:
                    char = "%"
                elif column == 55:
                    char = "="
                elif column == 56:
                    char = "="
                elif column == 57:
                    char = "@"
                elif column == 58:
                    char = "%"
                elif column == 59:
                    char = ":"
            elif row == 19:
                if column == 15:
                    char = "#"
                elif column == 16:
                    char = "@"
                elif column == 17:
                    char = "@"
                elif column == 18:
                    char = "%"
                elif column == 19:
                    char = "#"
                elif column == 20:
                    char = "@"
                elif column == 21:
                    char = "@"
                elif column == 22:
                    char = "-"
                elif column == 23:
                    char = "*"
                elif 24 <= column <= 34:
                    char = "@"
                elif column == 35:
                    char = "#"
                elif column == 36:
                    char = "*"
                elif column == 37:
                    char = ":"
                elif column == 38:
                    char = "."
                elif column == 39:
                    char = "."
                elif column == 40:
                    char = "@"
                elif column == 41:
                    char = "#"
                elif 42 <= column <= 51:
                    char = "@"
                elif column == 52:
                    char = "="
                elif column == 53:
                    char = "%"
                elif column == 54:
                    char = "*"
                elif column == 55:
                    char = "@"
                elif column == 56:
                    char = "%"
                elif column == 57:
                    char = "@"
                elif column == 58:
                    char = "@"
                elif column == 59:
                    char = "-"
            elif row == 20:
                if column == 15:
                    char = "-"
                elif column == 16:
                    char = "#"
                elif column == 17:
                    char = "@"
                elif column == 18:
                    char = "#"
                elif column == 19:
                    char = "-"
                elif column == 20:
                    char = "-"
                elif column == 21:
                    char = "="
                elif column == 22:
                    char = "."
                elif column == 23:
                    char = "="
                elif 24 <= column <= 33:
                    char = "@"
                elif column == 34:
                    char = "#"
                elif column == 35:
                    char = "*"
                elif column == 36:
                    char = ":"
                elif 37 <= column <= 39:
                    char = "."
                elif column == 40:
                    char = ":"
                elif column == 41:
                    char = "+"
                elif column == 42:
                    char = "%"
                elif 43 <= column <= 52:
                    char = "@"
                elif column == 53:
                    char = ":"
                elif column == 54:
                    char = "-"
                elif column == 55:
                    char = "*"
                elif column == 56:
                    char = "+"
                elif column == 57:
                    char = "#"
                elif column == 58:
                    char = "%"
                elif column == 59:
                    char = "-"
                elif column == 60:
                    char = "="
            elif row == 21:
                if column == 17:
                    char = "-"
                elif column == 18:
                    char = "="
                elif column == 19:
                    char = ":"
                elif column == 20:
                    char = "#"
                elif column == 21:
                    char = "+"
                elif column == 22:
                    char = "."
                elif column == 23:
                    char = "."
                elif column == 24:
                    char = "="
                elif 25 <= column <= 31:
                    char = "@"
                elif column == 32:
                    char = "#"
                elif column == 33:
                    char = "@"
                elif column == 34:
                    char = "*"
                elif 35 <= column <= 37:
                    char = "."
                elif 38 <= column <= 41:
                    char = ":"
                elif column == 42:
                    char = "%"
                elif column == 43:
                    char = "*"
                elif 44 <= column <= 53:
                    char = "@"
                elif column == 54:
                    char = "="
                elif column == 55:
                    char = ":"
                elif column == 56:
                    char = "%"
                elif column == 57:
                    char = "%"
                elif column == 58:
                    char = "="
                elif column == 59:
                    char = ":"
            elif row == 22:
                if column == 17:
                    char = ":"
                elif column == 18:
                    char = "*"
                elif column == 19:
                    char = "-"
                elif column == 20:
                    char = "="
                elif column == 21:
                    char = "*"
                elif column == 22:
                    char = "-"
                elif column == 23:
                    char = " "
                elif column == 24:
                    char = " "
                elif column == 25:
                    char = " "
                elif column == 26:
                    char = ":"
                elif column == 27:
                    char = "+"
                elif column == 28:
                    char = "#"
                elif column == 29:
                    char = "%"
                elif column == 30:
                    char = "*"
                elif column == 31:
                    char = "="
                elif column == 32:
                    char = "="
                elif column == 33:
                    char = "*"
                elif column == 34:
                    char = ":"
                elif column == 35:
                    char = "#"    
                elif 36 <= column <= 40:
                    char = "@"
                elif column == 41:
                    char = "#"
                elif column == 42:
                    char = "-"
                elif column == 43:
                    char = " "
                elif column == 44:
                    char = "-"
                elif column == 45:
                    char = "="
                elif column == 46:
                    char = "="
                elif column == 47:
                    char = "*"    
                elif column == 48:
                    char = "#"
                elif column == 49:
                    char = "+"
                elif column == 50:
                    char = "-"  
                elif column == 51:
                    char = " "
                elif column == 52:
                    char = " " 
                elif column == 53:
                    char = " "  
                elif column == 54:
                    char = "-"  
                elif column == 55:
                    char = "@"                         
                elif column == 56:
                    char = "*"
                elif column == 57:
                    char = "#"
                elif column == 58:
                    char = "+"
                elif column == 59:
                    char = "-"
            elif row == 23:
                if column == 17:
                    char = ":"
                elif column == 18:
                    char = "+"
                elif column == 19:
                    char = "%"
                elif column == 20:
                    char = ":"
                elif column == 21:
                    char = "+"
                elif column == 22:
                    char = "@"
                elif column == 23:
                    char = "="
                elif column == 24:
                    char = " "
                elif column == 25:
                    char = " "
                elif column == 26:
                    char = ":"
                elif column == 27:
                    char = " "
                elif column == 28:
                    char = " "
                elif column == 29:
                    char = " "
                elif column == 30:
                    char = " "
                elif column == 31:
                    char = " "
                elif column == 32:
                    char = " "
                elif column == 33:
                    char = " " 
                elif column == 34:
                    char = ":" 
                elif column == 35:
                    char = "#"                                  
                elif  36 <= column <= 41:
                    char = "@"
                elif column == 42:
                    char = "#"    
                elif column == 43:
                    char = ":"
                elif 44 <= column <= 52:
                    char = " "
                elif column == 53:
                    char = "+"
                elif column == 54:
                    char = "@"
                elif column == 55:
                    char = "@"
                elif column == 56:
                    char = "*"
                elif column == 57:
                    char = "#"
            elif row == 24:
                if column == 20:
                    char = "*"
                elif column == 21:
                    char = "+"
                elif column == 22:
                    char = "@"
                elif column == 23:
                    char = "@"
                elif column == 24:
                    char = "%"
                elif column == 25:
                    char = "="
                elif column == 30:
                    char = ":"
                elif column == 31:
                    char = "+"
                elif column == 32:
                    char = "%"
                elif 33 <= column <= 35:
                    char = "@"
                elif column == 36:
                    char = "-"
                elif column == 37:
                    char = "-"
                elif column == 38:
                    char = "+"
                elif column == 39:
                    char = "%"
                elif 40 <= column <= 42:
                    char = "@"
                elif column == 43:
                    char = "%"
                elif column == 44:
                    char = "="
                elif column == 49:
                    char = ":"
                elif column == 50:
                    char = "*"
                elif column == 51:
                    char = "@"
                elif column == 52:
                    char = "@"
                elif column == 53:
                    char = "%"
                elif column == 54:
                    char = "-"
                elif column == 55:
                    char = "+"
            elif row == 25:
                if column == 21:
                    char = "-"
                elif column == 22:
                    char = "%"
                elif column == 23:
                    char = "@"
                elif column == 24:
                    char = "@"
                elif column == 25:
                    char = "@"
                elif column == 26:
                    char = "#"
                elif column == 27:
                    char = "-"
                elif column == 30:
                    char = "+"
                elif column == 31:
                    char = "%"
                elif column == 32:
                    char = "@"
                elif column == 33:
                    char = "@"
                elif column == 34:
                    char = "*"
                elif 35 <= column <= 41:
                    char = "@"
                elif column == 42:
                    char = "%"
                elif 43 <= column <= 45:
                    char = "@"
                elif column == 46:
                    char = "#"
                elif column == 47:
                    char = ":"
                elif column == 48:
                    char = ":"
                elif column == 49:
                    char = "="
                elif 50 <= column <= 53:
                    char = "@"
                elif column == 54:
                    char = "#"
                elif column == 55:
                    char = "+"
                elif column == 56:
                    char = ":"
            elif row == 26:
                if column == 22:
                    char = "-"
                elif 23 <= column <= 27:
                    char = "@"
                elif column == 28:
                    char = "%"
                elif column == 29:
                    char = "-"
                elif 30 <= column <= 32:
                    char = "@"
                elif column == 33:
                    char = "#"
                elif column == 34:
                    char = "-"
                elif column == 35:
                    char = ":"
                elif 36 <= column <= 40:
                    char = "."
                elif column == 41:
                    char = ":"
                elif column == 42:
                    char = "#"
                elif 43 <= column <= 45:
                    char = "@"
                elif column == 46:
                    char = "%"
                elif column == 47:
                    char = "*"
                elif 48 <= column <= 52:
                    char = "@"
                elif column == 53:
                    char = "+"
                elif column == 54:
                    char = "-"
            elif row == 27:
                if column == 23:
                    char = ":"
                elif column == 24:
                    char = "%"
                elif 25 <= column <= 32:
                    char = "@"
                elif column == 33:
                    char = "#"
                elif column == 34:
                    char = "="
                elif column == 35:
                    char = "+"
                elif 36 <= column <= 41:
                    char = "@"
                elif column == 42:
                    char = "+"
                elif column == 43:
                    char = "+"
                elif column == 44:
                    char = "%"
                elif 45 <= column <= 52:
                    char = "@"
                elif column == 53:
                    char = "*"
            elif row == 28:
                if column == 24:
                    char = ":"
                elif column == 25:
                    char = "#"
                elif 26 <= column <= 32:
                    char = "@"
                elif column == 33:
                    char = "#"
                elif column == 34:
                    char = ":"
                elif column == 35:
                    char = "."
                elif column == 36:
                    char = "."
                elif 37 <= column <= 41:
                    char = ":"
                elif column == 42:
                    char = "."
                elif column == 43:
                    char = "."
                elif column == 44:
                    char = "+"
                elif 45 <= column <= 51:
                    char = "@"
                elif column == 52:
                    char = "*"
            elif row == 29:
                if column == 25:
                    char = ":"
                elif column == 26:
                    char = "%"
                elif 27 <= column <= 33:
                    char = "@"
                elif column == 34:
                    char = "%"
                elif column == 35:
                    char = "#"
                elif column == 36:
                    char = "="
                elif column == 37:
                    char = "*"
                elif column == 38:
                    char = "+"
                elif column == 39:
                    char = "*"
                elif column == 40:
                    char = "*"
                elif column == 41:
                    char = "-"
                elif column == 42:
                    char = "+"
                elif column == 43:
                    char = "+"
                elif column == 44:
                    char = "%"
                elif 45 <= column <= 51:
                    char = "@"
                elif column == 52:
                    char = "#"
                elif column == 53:
                    char = ":"
            elif row == 30:
                if column == 26:
                    char = "+"
                elif 27 <= column <= 50:
                    char = "@"
                elif column == 51:
                    char = "*"
                elif column == 52:
                    char = "+"
                elif column == 53:
                    char = ":"
            elif row == 31:
                if column == 24:
                    char = "+"
                elif column == 25:
                    char = "%"
                elif column == 26:
                    char = "#"
                elif column == 27:
                    char = "="
                elif column == 28:
                    char = "%"
                elif 29 <= column <= 51:
                    char = "@"
                elif column == 52:
                    char = "-"
                elif column == 53:
                    char = "-"
                elif column == 54:
                    char = "#"
                elif column == 55:
                    char = "@"
                elif column == 56:
                    char = "%"
                elif column == 57:
                    char = "-"
            elif row == 32:
                if column == 22:
                    char = "-"
                elif column == 23:
                    char = "#"
                elif column == 24:
                    char = "@"
                elif column == 25:
                    char = "="
                elif column == 26:
                    char = ":"
                elif column == 27:
                    char = "*"
                elif column == 28:
                    char = ":"
                elif column == 29:
                    char = "-"
                elif column == 30:
                    char = "#"
                elif 31 <= column <= 47:
                    char = "@"
                elif column == 48:
                    char = "%"
                elif column == 49:
                    char = "+"
                elif column == 50:
                    char = "="
                elif column == 51:
                    char = "%"
                elif column == 52:
                    char = "."
                elif column == 53:
                    char = "*"
                elif 54 <= column <= 57:
                    char = "@"
                elif column == 58:
                    char = "+"
            elif row == 33:
                if column == 19:
                    char = ":"
                elif column == 20:
                    char = "="
                elif column == 21:
                    char = "%"
                elif column == 22:
                    char = "@"
                elif column == 23:
                    char = "@"
                elif column == 24:
                    char = "@"
                elif column == 25:
                    char = "*"
                elif column == 26:
                    char = "."
                elif column == 27:
                    char = ":"
                elif column == 28:
                    char = "#"
                elif column == 29:
                    char = "%"
                elif column == 30:
                    char = "*"
                elif column == 31:
                    char = "#"
                elif 32 <= column <= 48:
                    char = "@"
                elif column == 49:
                    char = "*"
                elif column == 50:
                    char = ":"
                elif column == 51:
                    char = "."
                elif 52 <= column <= 57:
                    char = "@"
                elif column == 58:
                    char = "#"
                elif column == 59:
                    char = "-"
                elif column == 60:
                    char = ":"
            elif row == 34:
                if column == 13:
                    char = ":"
                elif column == 16:
                    char = ":"
                elif column == 17:
                    char = "*"
                elif 18 <= column <= 23:
                    char = "@"
                elif column == 24:
                    char = "@"
                elif column == 25:
                    char = "@"
                elif column == 26:
                    char = "@"
                elif column == 27:
                    char = "@"
                elif column == 28:
                    char = "@"
                elif column == 29:
                    char = "%"
                elif column == 30:
                    char = "*"
                elif column == 31:
                    char = "@"
                elif column == 32:
                    char = "%"
                elif column == 33:
                    char = "="
                elif column == 34:
                    char = ":"
                elif column == 35:
                    char = "="
                elif 36 <= column <= 50:
                    char = "@"
                elif column == 51:
                    char = "*"
                elif column == 52:
                    char = ":"
                elif 57 <= column <= 60:
                    char = "."
                elif column == 61:
                    char = "#"
                elif 62 <= column <= 70:
                    char = "@"
                elif column == 71:
                    char = "%"
                elif column == 72:
                    char = "%"
                elif column == 73:
                    char = "="
                elif column == 74:
                    char = ":"
            elif row == 35:
                if column == 12:
                    char = ":"
                elif column == 13:
                    char = "-"
                elif column == 14:
                    char = "+"
                elif column == 15:
                    char = "%"
                elif 16 <= column <= 24:
                    char = "@"
                elif column == 25:
                    char = "*"
                elif column == 26:
                    char = "@"
                elif column == 27:
                    char = "@"
                elif column == 28:
                    char = "+"
                elif column == 31:
                    char = ":"
                elif column == 32:
                    char = ":"
                elif column == 33:
                    char = "*"
                elif 34 <= column <= 42:
                    char = "@"
                elif column == 43:
                    char = "%"
                elif column == 44:
                    char = "-"
                elif 45 <= column <= 50:
                    char = "."
                elif column == 51:
                    char = "="
                elif 52 <= column <= 67:
                    char = "@"
                elif column == 68:
                    char = "%"
                elif column == 69:
                    char = "#"
                elif column == 70:
                    char = "+"
                elif column == 71:
                    char = "="
                elif column == 72:
                    char = "-"
                elif column == 73:
                    char = "-"
                elif column == 74:
                    char = ":"
            elif row == 36:
                if column == 8:
                    char = "-"
                elif column == 9:
                    char = "%"
                elif 10 <= column <= 34:
                    char = "@"
                elif column == 35:
                    char = "#"
                elif column == 36:
                    char = ":"
                elif 41 <= column <= 44:
                    char = "."
                elif column == 45:
                    char = ":"
                elif column == 46:
                    char = "-"
                elif 47 <= column <= 51:
                    char = "@"
                elif column == 52:
                    char = "%"
                elif column == 53:
                    char = ":"
                elif 61 <= column <= 67:
                    char = "."
                elif column == 68:
                    char = ":"
                elif 69 <= column <= 93:
                    char = "@"
                elif column == 94:
                    char = "#"
                elif column == 95:
                    char = "-"
            elif row == 37:
                if column == 3:
                    char = ":"
                elif column == 4:
                    char = "="
                elif column == 5:
                    char = "#"
                elif column == 6:
                    char = "%"
                elif 7 <= column <= 31:
                    char = "@"
                elif column == 32:
                    char = "+"
                elif 41 <= column <= 42:
                    char = ":"
                elif column == 43:
                    char = "-"
                elif column == 44:
                    char = "+"
                elif column == 54:
                    char = "="
                elif 55 <= column <= 79:
                    char = "@"
            elif row == 38:
                if 0 <= column <= 26:
                    char = "@"
                elif column == 27:
                    char = "%"
                elif column == 28:
                    char = ":"
                elif 29 <= column <= 35:
                    char = "."
                elif column == 36:
                    char = ":"
                elif column == 37:
                    char = "*"
                elif column == 38:
                    char = "@"
                elif column == 39:
                    char = "@"
                elif column == 40:
                    char = "%"
                elif column == 41:
                    char = ":"
                elif 42 <= column <= 49:
                    char = "."
                elif 50 <= column <= 79:
                    char = "@"

            print(char, end="")
        print()


generate_ascii_art()
