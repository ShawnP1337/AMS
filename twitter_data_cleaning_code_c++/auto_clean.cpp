#include <string>
#include <iostream>
#include <filesystem>
#include <thread>
#include <vector>
#include "tweet_clean_util.cpp"
namespace fs = std::filesystem;

int main() {
    //std::string path_folders = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_14_Twitter_Data";
    std::string path_folders = "D:\\Documents\\Coding\\C++\\twitter_data_cleaning\\testsets\\final";
    
    std::string filepath;
    std::vector<std::thread> threads;
    int numThreads = std::thread::hardware_concurrency();
    int count = 0;

    //std::string path_folders = "C:/Users/awyat049/OneDrive/Documents/Coding/2022_11_14_Twitter_Data";

    for (const auto &entry : fs::directory_iterator(path_folders)) {
        for (const auto &file : fs::directory_iterator(entry.path())) {
            filepath = (file.path()).string();
            threads.push_back(std::thread(clean_file,filepath));
            //clean_file(filepath);
            if (count == 4*numThreads) {
                for (auto &th : threads) {
                    th.join();
                }
                count = 0;
                threads.clear();
            }
            count++;
        }

    }
    for (auto &th : threads) {
                    th.join();
                }
                count = 0;
                threads.clear();

    return 0;
}
