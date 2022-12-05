#include <iostream>
#include <fstream>
#include <locale>
#include <string>
#include <vector>
#include <sstream>
#include <utility>
#include <stdexcept>
#include <regex>

// This is used to create text files to generate wordclouds from

int static numvalcol = 8;

std::string get_csv_column(std::ifstream &in)
{
    // so this is the actual reading object passed here
    // this function looks at one block and returns when it hits an appropriate point (measure by conditions)
    // thus, when it returns, we are at the exact place in the reader where it returns
    std::string col;
    unsigned quotes = 0;
    char prev = 0;
    bool finis = false;

    for (int ch; !finis && (ch = in.get()) != EOF; ) {
        switch(ch) {
        case '"':
            ++quotes;
            break;
        case ',':
            if (quotes == 0 || (prev == '"' && (quotes & 1) == 0)) {
                finis = true;
            }
            break;
        case '\n':
            if (quotes == 0|| ((quotes & 1) == 0)) {
                finis = true;
            }
            break;
        default:;
        }
        ch = std::tolower(ch);
        col += prev = ch;
    }
    return col;
}

/* std::string split_last_col(std::ifstream &in) {
    std::istringstream iss (term);
    std::string tmp;

    while (iss >> tmp) {
} */


std::vector<std::string> csv_reader(std::string filepath) {
    std::ifstream myFile(filepath);

    if(!myFile.is_open()) throw std::runtime_error("Could not open file");

    std::vector<std::string> result;
    //int count = 0;

    for (std::string col; myFile; ) {
/*         if (count == (numvalcol - 1)) {
            count = -1;
            std::istringstream iss(myFile);
            std::string temp;

            while (iss >> temp) {
                col = get_csv_column(temp);

            }
        }
        else { */

        col = get_csv_column(myFile);
        result.push_back(col);

        //std::cout << col << std::endl;
        //}
    }

    myFile.close();

    //std::cout << result.size();

    return result;
}

std::string cleantweet(std::string term, std::string tweet) {

    std::string text = "";
    std::string currword;
    std::string currterm;
    std::istringstream iss(tweet);
    int count = 0;

    while (iss >> currword) {
        std::istringstream is2(term);

        while(is2 >> currterm) {
            if ((currword.find(currterm) != std::string::npos)) {
                count++;
            }
        }
        if (count == 0) {
            text = text + currword + " ";
        }
        count = 0;
    }

    return text;
}

std::string removecode(std::string tweet) {

    size_t pos = std::string::npos;
    std::string toErase = "&amp";

    while ((pos  = tweet.find(toErase) )!= std::string::npos) {
        // If found then erase it from string
        tweet.erase(pos, toErase.length());
    }

    std::string final = "";

    for (auto c : tweet){
         if (!ispunct(c)){
            final = final + c;
         }
    }

    std::regex length2 ("\\b\\w{1,2}\\b");

    return std::regex_replace(final,length2, "");
}


// also clean tweets in here, if correct column number for tweet content, call cleaner function
int csv_writer(std::string filename, std::vector<std::string> vals) {

    std::ofstream myFile(filename+"_tweets_no_term.txt");

    int numrows = vals.size();
    int counter = 0 - numvalcol;
    std::string cleaned;

    //put term used to scrape tweet here
    std::string term = "standard living http"; // CHANGE HERE ---------------------------------------------------------

    for(std::string i : vals) {

        if (counter == 1) {
            cleaned = cleantweet(term,i);
            cleaned = removecode(cleaned);
            myFile << cleaned << "\n";  
            //std::cout << cleaned;
        }
        else if (counter == numvalcol - 1) {
            counter = -1;
        } 
        counter++; 
    }
    myFile.close();
    
    return 0;
}

int clean_file(std::string filepathin,std::string filepathout) {

    std::vector<std::string> data = csv_reader(filepathin);
    csv_writer(filepathout, data);

    return 0;
}

int main () {
    // set filepathin to file to read
    std::string basepath = "C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_29_Final_Data_Full\\";
    std::string filepathin = basepath + "standard_of_living_sentiment.csv"; // CHANGE HERE ---------------------------------------------------------
    std::string filepathout = "standard_of_living"; // CHANGE HERE ---------------------------------------------------------

    clean_file(filepathin, filepathout);
}

/// TO DO -- remove \n, ', &amp other things that show up in all word clouds, then generate again

