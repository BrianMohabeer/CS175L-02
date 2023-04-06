#Brian Mohabeer
#CS175L
#WorldSeries

def main():
    world_series_list=create_list()
    search_team = input("Enter the name of the team or Quit: ")
    while search_team != "Quit" and search_team != "quit":
        search_list(world_series_list, search_team)
        search_team = input("Enter the name of the team or Quit: ")
    
def create_list():
    file = open('WorldSeriesWinners.txt', 'r')
    world_series_list = []
    x = 0
    for line in file:
        world_series_list.append(line.rstrip())
        x = x + 1
    file.close()
    return world_series_list

def search_list(world_series_list, search_team):
    count = 0
    for team in world_series_list:
        if search_team.upper() in team.upper():
            count = count + 1
    if count >= 1:
        print(f"The {search_team} won the world series {count} times between 1903 and 2009")
    else:
        print("This team either did not win the world series or you entered an invalid input")
            
        

if __name__ == '__main__':
    main()
