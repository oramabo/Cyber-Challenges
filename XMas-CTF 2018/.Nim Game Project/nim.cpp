#include<iostream>
#include<vector>

//  Future Project!

const int NOPILES = 15;

enum class Turns
{
    MY,
    COMPUTER
};

enum class GameStates
{
    WIN,
    LOSS,
    ONGOING
};

class Heap
{
private:
    int sum;
public:
    std::vector<int> stones;
    Heap()
    {
        for(int i = 0; i < NOPILES; i++)
        {
            stones.push_back(1);
        }
    }
};

class Nim
{
public:
    Heap nheap;
    Turns turn;
    GameStates state;
    Nim()
    {
        turn = Turns::MY;
        state = GameStates::ONGOING;
    }
    void changeTurn()
    {
        turn == Turns::MY ? turn = Turns::COMPUTER : turn = Turns::MY;
    }
    void menu();
};

void Nim::menu()
{
    while(state == GameStates::ONGOING)
    {
        changeTurn();
        break;
    }
}

int main()
{
    Nim a;
    a.menu();
    return 0;
}
