from GameFunctions import *
from deck import game_deck

# main function
def main():

    #variables for the Game
    stay_or_hit = 0
    all_cards = game_deck()
    player_hand = []
    dealer_hand = []
    player_stays = True
    dealer_stays = True

    #give both players cards
    for _ in range(2):
        deal_card(player_hand, all_cards)
        deal_card(dealer_hand, all_cards)

    #while loop for the game
    while player_stays or dealer_stays:
        print(f"Dealer has\n {print_hand(reveal_dealer_hand(dealer_hand))}\nand hidden card(s)\n")
        print(f"Your hand is:\n {print_hand(player_hand)}")
        if player_stays:
            stay_or_hit = input("press 1 to Stay,everything else to Hit \n")
        if total(dealer_hand) > 16:
            dealer_stays = False
        else:
            deal_card(dealer_hand,all_cards)
        if stay_or_hit == "1":
            player_stays = False
        else:
            deal_card(player_hand,all_cards)
        if total(player_hand) >= 21:
            break
        elif total(dealer_hand) >= 21:
            break

    if total(player_hand) == 21:
        print(f"\n You have \n {print_hand(player_hand)}of an total of {total(player_hand)} \n \nand the dealer has \n {print_hand(dealer_hand)}for a total of {total(dealer_hand)}")
        print("BLACKJaCK! You win!!!!! :D")
    elif total(dealer_hand) == 21:
        print(f"\n You have \n {print_hand(player_hand)}of an total of {total(player_hand)} \n \nand the dealer has \n {print_hand(dealer_hand)}for a total of {total(dealer_hand)}")
        print("BLACKJaCK! You lost :,(")
    elif total(player_hand) > 21:
        print(f"\n You have \n {print_hand(player_hand)}of an total of {total(player_hand)} \n \nand the dealer has \n {print_hand(dealer_hand)}for a total of {total(dealer_hand)}")
        print("You bust! You lost :,(")
    elif total(dealer_hand) > 21:
        print(f"\n You have \n {print_hand(player_hand)}of an total of {total(player_hand)} \n \nand the dealer has \n {print_hand(dealer_hand)}for a total of {total(dealer_hand)}")
        print("Dealer busts! You Win!! :)")
    else:
        print("You are nearer on 21, You win :)") if 21 - total(player_hand) < 21 - total(dealer_hand) else print("Dealer is nearer on 21, He wins :(")

    if input("1: replay\n") == "1":
        main()
    else:
        return 0


#run the main function
if __name__ == '__main__':
    main()
