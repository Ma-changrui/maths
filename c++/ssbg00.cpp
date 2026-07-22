#include "ssbg.h"
#include <iostream>
#include <limits>
#include <vector>
#include <tuple>
#include <numeric>

using namespace std;  

bool choice_language() {
    cout << "选择语言/Select Language (1-中文, 2-English): ";
    int choose;
    while (true) {
        if (!(cin >> choose)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "无效输入，请重新选择 (1 或 2): ";
        } else if (choose == 1) {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return true;
        } else if (choose == 2) {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return false;
        } else {
            cout << "选择错误，请重新输入 (1 或 2): ";
        }
    }
}

string L(const string& cn, const string& en, bool lang) {
    return lang ? en : cn;
}

vector<decimal_t> user_input(bool lang) {
    vector<decimal_t> numbers;
    string line;
    while (true) {
        cout << L("输入数字(输入q退出): ", "Enter a number (enter q to quit): ", lang);
        if (!getline(cin, line)) break;

        // 去除首尾空白
        line.erase(0, line.find_first_not_of(" \t\r\n"));
        line.erase(line.find_last_not_of(" \t\r\n") + 1);

        if (line.empty()) continue;                       // 跳过空行
        if (line.find_first_of("qQ") != string::npos) break;

        try {
            decimal_t num{line};
            numbers.push_back(num);
        } catch (const runtime_error&) {
            cout << L("无效数字，请重新输入。",
                      "Invalid number, please try again.", lang) << endl;
        }
    }
    return numbers;
}

vector<decimal_t> get_input(int const min_count, bool const lang) {
    while (true) {
        auto numbers = user_input(lang);
        if (numbers.size() >= static_cast<size_t>(min_count)) {
            return numbers;
        }
        cout << L("至少需要输入 " + to_string(min_count) + " 个数字，请重新输入。\n",
                  "At least " + to_string(min_count) + " numbers are required, please re-enter.\n",
                  lang);
    }
}

std::vector<GroupResult> average_value(const std::vector<decimal_t>& data) {
    int n = static_cast<int>(data.size());
    std::vector<GroupResult> results;

    for (int i = 0; i < n - 1; ++i) {
    
        std::vector<decimal_t> left(data.begin(), data.begin() + i + 1);
        std::vector<decimal_t> right(data.begin() + i + 1, data.end());

        // 计算总和
        decimal_t left_sum  = std::accumulate(left.begin(), left.end(), decimal_t(0));
        decimal_t right_sum = std::accumulate(right.begin(), right.end(), decimal_t(0));

        // 计算均值
        decimal_t left_mean  = left_sum / left.size();
        decimal_t right_mean = right_sum / right.size();

        results.push_back({i, std::move(left), std::move(right), left_mean, right_mean});
    }
    return results;
}