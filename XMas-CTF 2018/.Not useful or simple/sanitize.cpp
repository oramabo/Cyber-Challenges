#include<iostream>
#include<vector>
#include<algorithm>

std::string clean(std::string x, std::string rm)
{
    while(x.find(rm)!=std::string::npos)
    {
        int loc = x.find(rm);
        x.erase(loc, rm.length());
    }
    return x;
}

int main()
{
    std::vector<std::string> crit = {" ", ",", "."};
    std::string san = "vF ur uNq nAlguvat pbasvqraGvNy gb fnl, ur jebgr Vg ia pvcure, gung vF, ol FB punaTvat gur beqre bs gur Yrggref bs gur nycuNorg, gung abg n jbeQ pbhyq or ZnQR bHg.";
    transform(san.begin(), san.end(), san.begin(), ::tolower);
    for(std::size_t i = 0; i < crit.size(); i++)
    {
        san = clean(san, crit[i]);
    }
    san = "X-MAS{" + san + "}";
    std::cout << san << "\n";
    return 0;
}
