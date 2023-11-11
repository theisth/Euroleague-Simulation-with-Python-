#Euroleague Simulation Project with OOP

my_name = 'Ahmet Ali Tilkicioglu'
my_id = '210102002163'
my_email = 'a.tilkicioglu2021@gtu.edu.tr' 

import random

class Person:

    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

    def get_name(self):
        return self.name + ' ' + self.lastname

    def __str__(self):
        return self.name + ' ' + self.lastname

    def __lt__(self,other):
        if self.lastname == other.lastname:
            return self.name < other.lastname
        else:
            return self.lastname < other.lastname


class Player(Person):
    player_id = 0

    def __init__(self,name,lastname):
        Person.__init__(self,name,lastname)
        self.power = random.randint(4,8)
        self.score = []
        a = 0
        for i in self.score:
            a = a + i
        self.total_score = a
        Player.player_id += 1
        self.id = Player.player_id 

    def get_power(self):
        return self.power
    
    def add_to_points(self,x):
        self.score.append(x)
    
    def get_points_detailed(self):
        return self.score

    def get_points(self):
        if self.score == []:
            return 0
            
        sum = 0
        for i in self.score:
            sum = sum + i
        
        return sum

    def reset(self):
        self.score.clear()

    def __lt__(self,other):

        if self.total_score != other.total_score:
            return self.total_score <  other.total_score
        
        if self.lastname != other.lastname:
            return self.lastname < other.lastname

        if self.name != other.name:
            return self.name < other.name

    def get_week_score(self,x):
        return self.score[x-1]

    def add_ex_point(self,x):
        self.score[-1] = self.score[-1] + x

    def get_id(self):
        return self.id 

    def set_team(self,t):
        Team.player_add(t,self)


             
class Manager(Person):
    manager_id = 0

    def __init__(self, name, lastname):
        Person.__init__(self,name,lastname)
        self.manager_score = []
        self.total_manager_score = 0
        Manager.manager_id += 1
        self.id = Manager.manager_id

        for i in self.manager_score:
            self.total_manager_score += i
        
    def reset(self):
        self.total_manager_score = 0
        self.manager_score.clear()

    def add_influence(self,x):
        self.manager_score.append(x)

    def get_influence_detailed(self):
        return self.manager_score

    def get_influence(self):
        o = 0
        for i in self.manager_score:
            o += i
        self.total_manager_score = o
        return o

    
    def get_influence_week(self,x):
        return self.manager_score[x-1]
    
    def __lt__(self,other):

        if self.total_manager_score != other.total_manager_score:
            return self.total_manager_score < other.total_manager_score
        
        if self.lastname != other.lastname:
            return self.lastname < other.lastname

        if self.name != other.name:
            return self.name < other.name

    def set_team(self,t):
        Team.set_manager(t,self) 

    def get_id(self):
        return self.id


class Team:
    team_id = 0

    def __init__(self,teamname,manager,players):
        self.teamname = teamname
        self.manager = manager
        self.players = players

        self.score_list = []
        self.total_score = 0
        self.conceded_score = 0
        self.wins = 0
        self.loses = 0
        Team.team_id += 1
        self.id = Team.team_id 
        self.matches = [] 


    def get_name(self):
        return self.teamname

    def get_manager(self):
        return self.manager

    def get_roster(self):
        return self.players

    def reset(self):
        for i in self.players:
            Player.reset(i)
        Manager.reset(self.manager)

    def add_score(self,x):
        self.score_list.append(x)
        self.total_score += x
    
    def add_conceded_score(self,x):
        self.conceded_score += x
    
    def get_scored(self):
        oo = 0
        for i in self.score_list:
            oo += i

        self.total_score = oo
        return oo 

    
    def get_conceded(self):
        return self.conceded_score
    
    def add_wins(self):
        self.wins += 1
    
    def add_losses(self):
        self.loses += 1
    
    def get_wins(self):
        return self.wins
    
    def get_losses(self):
        return self.loses
    
    def __str__(self):
        return self.teamname

    def __lt__(self,other):

        if self.total_score != other.total_score:
            return self.total_score < other.total_score
        
        if (self.total_score - self.conceded_score) != (other.total_score - other.conceded_score):
            return (self.total_score - self.conceded_score) < (other.total_score - other.conceded_score)

    def add_result(self,s):
        self.total_score += s[0]
        self.conceded_score += s[1]
        self.score_list.append(s[0])

        if s[0] > s[1]:
            Team.add_wins(self)
        else:
            Team.add_losses(self)

    
    def get_team_week_score(self,x):
        return self.score_list[x-1]

    def set_manager(self,x):
        self.manager = x

    def get_id(self):
        return self.id

    def player_add(self,x):
        self.players.append(x) 
    
    def get_points_detailed(self):
        return self.score_list


class Match:

    def __init__(self,home_team,away_team,week_no):
        self.home = home_team
        self.away = away_team
        self.week = week_no
        self.total_score_home = 0
        self.total_score_away = 0
        self.played = 0

    def is_played(self):
        if self.played == 0:
            return False
        else:
            return True


    def play(self):

        if self.played == 1:
            return None 

        home_manager_points = random.randint(-10,10)
        away_manager_points = random.randint(-10,10)
        total_home = 0
        total_away = 0

        for i in Team.get_roster(self.home):
            player_point = 0
            for nothing in range(4):
                uu = 0
                pwr = Player.get_power(i)
                r = random.randint(-5,5) 
                uu = pwr + r
                total_home += uu
                player_point += uu
            Player.add_to_points(i,player_point)

        for i in Team.get_roster(self.away):
            player_point2 = 0
            for nothing in range(4):
                uu2 = 0
                pwr2 = Player.get_power(i)
                r2 = random.randint(-5,5)
                uu2 = r2 + pwr2
                total_away  += uu2
                player_point2 += uu2
            Player.add_to_points(i,player_point2)
        
        hm = Team.get_manager(self.home)
        aw = Team.get_manager(self.away)

        Manager.add_influence(hm,home_manager_points)
        Manager.add_influence(aw,away_manager_points)
        
        total_home += home_manager_points
        total_away += away_manager_points

        while total_away == total_home:

            for i in Team.get_roster(self.home):
                player_point = 0
                for nothing in range(1):
                    uu = 0
                    pwr = Player.get_power(i)
                    r = random.randint(-5,5) 
                    uu = pwr + r
                    total_home += uu
                    player_point += uu
                Player.add_ex_point(i,player_point)

            for i in Team.get_roster(self.away):
                player_point2 = 0
                for nothing in range(1):
                    uu2 = 0
                    pwr2 = Player.get_power(i)
                    r2 = random.randint(-5,5)
                    uu2 = r2 + pwr2
                    total_away  += uu2
                    player_point += uu2
                Player.add_ex_point(i,player_point2)

        self.total_score_home += total_home
        self.total_score_away += total_away

        Team.add_score(self.home,self.total_score_home)
        Team.add_score(self.away,self.total_score_away)

        Team.add_conceded_score(self.home,self.total_score_away)
        Team.add_conceded_score(self.away,self.total_score_home)

        if total_home > total_away:
            Team.add_wins(self.home)
            Team.add_losses(self.away)
        else:
            Team.add_wins(self.away)
            Team.add_losses(self.home)

        self.played += 1
        return None

    def get_match_score(self):
        return (self.total_score_home,self.total_score_away)

    def get_teams(self):
        return (self.home,self.away) 

    def get_home_team(self):
        return Team.get_name(self.home)

    def get_away_team(self):
        return Team.get_name(self.away)

    def get_winner(self):

        if self.played == 0:
            return None
        
        if self.total_score_home < self.total_score_away:
            return Team.get_name(self.away)
        else:
            return Team.get_name(self.home)

    def __str__(self):
        h = Team.get_name(self.home)
        a = Team.get_name(self.away)
        h_scr = (self.total_score_home)
        a_scr = (self.total_score_away)

        if self.played == 0:
            return h + ' ' + 'vs.' + ' ' + a
        else:
            return h + ' ' +'(' + str(h_scr) + ')' + ' ' + 'vs.' + ' ' + '(' + str(a_scr) + ')' + ' ' + a


class Season:

    def __init__(self,teams,managers,players):
        self.managers = managers
        self.players = players
        self.teams = teams
        self.man_list = []
        self.ply_list = []
        self.edited_ply_list = []
        self.tm_list_name = []
        self.completed_team_list = []
        random.shuffle(self.completed_team_list)
        self.fix_match = []
        self.week_no = 1
        if self.week_no > len(self.fix_match):
            self.week_no = len(self.fix_match) 

        
        with open(self.players) as f:
            for i in f.readlines():
                a = i.strip('\n')
                ed = a.split(' ')
                comp = Player(ed[0],ed[1])
                self.ply_list.append(comp)

        aa = 0
        for i in range(len(self.ply_list)//5):
            self.edited_ply_list.append(self.ply_list[aa:aa+5])
            aa += 5


        with open(self.managers)as f1:
            for i in f1.readlines():
                a = i.strip('\n')
                ed = a.split(' ')
                comp = Manager(ed[0],ed[1])
                self.man_list.append(comp)

        with open(self.teams) as f2:
            for i in f2.readlines():
                a = i.strip('\n')
                self.tm_list_name.append(a)

        uu = 0
        for i in self.tm_list_name:
            w = Team(i,self.man_list[uu],self.edited_ply_list[uu])
            self.completed_team_list.append(w)
            uu = uu + 1


    def get_players(self):
        return self.ply_list
    
    def get_managers(self):
        return self.man_list
    
    def get_teams(self):
        return self.completed_team_list
    
    def get_season_lenght(self):
        return len(self.fix_match)
    
    def build_fixture(self):
        n = len(self.completed_team_list)
        matchs = []
        fixtures = []
        return_matchs = []
        for fixture in range(1, n):
            for i in range(n//2):
                matchs.append((self.completed_team_list[i], self.completed_team_list[n - 1 - i]))
                return_matchs.append((self.completed_team_list[n - 1 - i], self.completed_team_list[i]))
            self.completed_team_list.insert(1, self.completed_team_list.pop())
            fixtures.insert(len(fixtures)//2, matchs)
            fixtures.append(return_matchs)
            matchs = []
            return_matchs = []

            ch = []
        for fixture in fixtures:
            ch.append(fixture)


        no_week = 0
        for i in ch:
            no_week += 1
            spc = []
            for j in i:
                rr = Match(j[0],j[1],no_week)
                spc.append(rr)
            self.fix_match.append(spc) 

    def get_fixture(self,week_no):
        return self.fix_match[week_no-1]

    def get_week_no(self):
        return self.week_no

    def play_week(self):

        tt = self.fix_match[self.week_no-1]
        for i in tt:
            Match.play(i)
        self.week_no += 1

    def get_champion(self):
        
        if self.week_no == Season.get_season_lenght(self):
            ss = []
            for i in self.completed_team_list:
                ss.append(Team.get_wins(i))
            x = ss.index(max(ss))
            return self.completed_team_list[x]
        else:
            return None

    def reset(self):
        self.man_list = []
        self.ply_list = []
        self.edited_ply_list = []
        self.tm_list_name = []
        self.completed_team_list = []
        self.fix_match = []
        self.week_no = 1
    
    def get_best_player(self):
        ss = []
        for i in self.ply_list:
            ss.append(Player.get_week_score(i,self.week_no))
        x = ss.index(max(ss))
        return self.ply_list[x]

    def get_best_manager(self):
        ss = []
        for i in self.man_list:
            ss.append(Manager.get_influence_week(i,self.week_no))
        x = ss.index(max(ss))
        return self.man_list[x]

    def get_most_scoring_team(self):
        ss = []
        for i in self.completed_team_list:
            ss.append(Team.get_team_week_score(i,self.week_no))
        x = ss.index(max(ss))
        return self.completed_team_list[x]

    def get_all_fixture(self):
        return self.fix_match 

if __name__ == "__main__":

    teams_file = 'teams.txt'
    managers_file = 'managers.txt'
    players_file = 'players.txt'

    # Create a season
    season21 = Season(teams_file, managers_file, players_file)
    season21.build_fixture()

    # Play the matches
    for i in range(season21.get_season_lenght()):
        season21.play_week()



# Get season statistics
print("Champion is:", season21.get_champion() )
print("Champion Wins:", Team.get_wins(season21.get_champion()))
print("/////////////////////////////")
print("Champion Roster:")
for i in Team.get_roster(season21.get_champion()):
    print(i)
print("/////////////////////////////")
print("Most scoring team is:", season21.get_most_scoring_team() )
print("MVP League:", season21.get_best_player() )
print("Best manager is:", season21.get_best_manager() )

