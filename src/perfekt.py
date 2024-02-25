def main():
    
    with open("data/output/irregular_perfekt.txt", 'w') as file_out:
        with open("data/input/irregular_verben.txt", "r") as file_in:
            for line in file_in:
                line = line.split()
                
                for index, item in enumerate(line):
                    if item[0].isupper():
                        break
                index -= 1
                
                line = f"{line[0]};{line[index]}<br><br><i>{' '.join(line[(index+1):])}</i>\n"
                file_out.write(line)
    
if __name__ ==  "__main__":
    main()