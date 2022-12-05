#include <iostream>
#include <string>
#include <sstream>
#include <regex>

std::string remove_hashtag(std::string tweet) {
    std::regex hashtag ("#+[a-zA-Z0-9(_)]{1,}");

    return std::regex_replace(tweet,hashtag, "");
}

std::string remove_at(std::string tweet) {
    std::regex at ("@+[a-zA-Z0-9(_)]{1,}");

    return std::regex_replace(tweet,at, "");
}

std::string check_match(std::string term, std::string tweet) {
    std::istringstream iss (term);
    std::string tmp;

    while (iss >> tmp) {
        if (std::regex_search(tweet, std::regex(tmp))) {
            continue;
        }
        return "";
    }

    return tweet;
}

std::string cleantweet(std::string term, std::string tweet) {

    std::string tweetnohash = remove_hashtag(tweet);
    std::string tweetclean = remove_at(tweetnohash);
    return check_match(term, tweetclean);
}

/* int main() {

    std::istringstream iss ("0\n2016-11-09");
    std::string tmp;
    int n = 0;

    while (iss >> tmp) {
        std::cout << "num: " + n + tmp + "\n";
        n++;
    }

    //std::cout << cleantweet("housing", "@17days17goals #SDG11 By 2030, ensure access for all to adequate, safe and affordable housing and basic services and upgrade slums");
}  */