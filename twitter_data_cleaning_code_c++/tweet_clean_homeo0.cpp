#include <iostream>
#include <fstream>
#include <locale>
#include <string>
#include <vector>
#include <sstream>
#include <utility>
#include <stdexcept>
#include <filesystem>
#include <thread>
#include "clean_tweets.cpp"
namespace fs = std::filesystem;

int static numvalcol = 7;

std::string get_csv_column(std::ifstream &in)
{
    // so this is the actual reading object passed here
    // this function looks at one block and returns when it hits an appropriate point (measure by conditions)
    // thus, when it returns, we are at the exact place in the reader where it returns
    // Therefore, to fix, I just need to get it to also return in the situation where there's a new line character
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

std::string get_term(std::string filename) {
    std::string term;

    for (char &c : filename) {
        switch(c) {
        case '[':
            goto end_loop;
        case '_':
            c = ' ';
        default:;
        }
        c = std::tolower(c);
        term += c;
    }
    end_loop: ;

    std::cout << term << "\n";

    return term;
}

std::string get_filename(std::string path) {
    std::string filename;
    std::string base_filename = path.substr(path.find_last_of("/\\") + 1);
    std::string::size_type const p(base_filename.find_last_of('.'));
    return base_filename.substr(0, p);
}


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


// also clean tweets in here, if correct column number for tweet content, call cleaner function
int csv_writer(std::string filename, std::vector<std::string> vals) {

    std::ofstream myFile(filename+"_clean.csv");

    int numrows = vals.size();
    int counter = 0 - numvalcol;
    bool skip = false;
    std::string cleaned;

    std::string term = "home owner";

    for(std::string i : vals) {


        if (counter < 0) {
            if (counter == -1) {
                myFile << i;
            }
            else {
                myFile << i;
            }
        }
        else if (skip == true) {
            if (counter == numvalcol - 1) {
                myFile << "\n";
                counter = -1;
                skip = false;
            }
        }
        else if (counter == numvalcol - 1) {
            myFile << i;
            counter = -1;
            //std::cout << counter;
        } 
        else if (counter == 1) {
            cleaned = cleantweet(term,i);
            if (cleaned == "") {
                skip = true;
                //myFile << ",";
            } // make sure this isn't accidentally skipping other tweets // TO DO
            else {
                myFile << cleaned;
            }  
        }
        else {
            myFile << i;
        }
        //std::cout << counter;
        //std::cout << " : " + i;
        counter++; 
        //std::cout << counter;
    }
    myFile.close();
    
    return 0;
}

int clean_file(std::string filepath) {
    std::string filename = get_filename(filepath);

    //std::cout << filename;


    std::vector<std::string> data = csv_reader(filepath);
    csv_writer(filename, data);

    return 0;
}

int main() {

    clean_file("C:\\Users\\awyat049\\OneDrive\\Documents\\Coding\\2022_11_14_Twitter_Data\\home Owner\\home_owner[datetime.date(2016_10_28), datetime.date(2016_10_31)].csv");
    return 0;
}

