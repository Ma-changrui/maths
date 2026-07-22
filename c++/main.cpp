#include "ssbg.h"
#include <iostream>
#include <windows.h>
#include <exception>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    try {
        bool lang = choice_language();

        auto numbers = get_input(2, lang);

        auto groups = average_value(numbers);

        // ----- 输出所有输入的数字 -----
        cout << L("\n输入的数字: ", "\nInput numbers: ", lang);
        for (const auto& num : numbers) {
            cout << num << " ";
        }
        cout << "\n" << string(48, '─') << "\n";

        // ----- 存储所有分组结果 (SSW, 左组, 右组) -----
        struct SswResult { decimal_t ssw; vector<decimal_t> left; vector<decimal_t> right; };
        vector<SswResult> results;

   
        for (const auto& group : groups) {
            int    i          = group.index;
            const auto& left  = group.left;
            const auto& right = group.right;
            decimal_t left_mean  = group.left_mean;
            decimal_t right_mean = group.right_mean;

            // 计算 SSW = Σ(x - mean)²
            decimal_t ssw = 0;
            for (const auto& x : left) {
                decimal_t diff = x - left_mean;
                ssw += diff * diff;
            }
            for (const auto& x : right) {
                decimal_t diff = x - right_mean;
                ssw += diff * diff;
            }

            // 输出当前分组信息
            cout << L("方案 ", "Plan ", lang) << (i + 1) << "\n";
            cout << L("  左组: ", "  Left: ", lang);
            for (size_t j = 0; j < left.size(); ++j) {
                cout << left[j] << (j + 1 == left.size() ? "" : ", ");
            }
            cout << "\n";
            cout << L("  右组: ", "  Right: ", lang);
            for (size_t j = 0; j < right.size(); ++j) {
                cout << right[j] << (j + 1 == right.size() ? "" : ", ");
            }
            cout << "\n";
            cout << "  SSW = " << ssw << "\n";
            cout << string(48, '─') << "\n";

            // 保存结果用于最后找最优
            results.push_back({ssw, left, right});
        }

        // ----- 找最优分组（SSW 最小）-----
        if (results.empty()) {
            cout << L("\n没有可用的分组结果，程序退出。",
                      "\nNo available grouping results, exiting.", lang) << "\n";
            return 0;
        }

        auto best = min_element(results.begin(), results.end(),
            [](const auto& a, const auto& b) {
                return a.ssw < b.ssw;
            });

        decimal_t best_ssw = best->ssw;
        vector<decimal_t> best_left = best->left;
        vector<decimal_t> best_right = best->right;

        // ----- 输出最优结果 -----
        cout << L("\n", "\n", lang);
        cout << L("✨ 最优分组 ", "✨ Best Grouping ", lang);
        cout << string(48, '=') << "\n";

        cout << L("  左组: ", "  Left: ", lang);
        for (size_t j = 0; j < best_left.size(); ++j) {
            cout << best_left[j] << (j + 1 == best_left.size() ? "" : ", ");
        }
        cout << "\n";

        cout << L("  右组: ", "  Right: ", lang);
        for (size_t j = 0; j < best_right.size(); ++j) {
            cout << best_right[j] << (j + 1 == best_right.size() ? "" : ", ");
        }
        cout << "\n";

        cout << L("  最小组内离差平方和 = ", "  Minimum SSW = ", lang) << best_ssw << "\n";

        
        double best_ssw_d = best_ssw.convert_to<double>();
        if (best_ssw_d <= 10) {
            cout << L("  四舍五入到 0.0001 = ", "  Rounded to 0.0001 = ", lang)
                 << fixed << setprecision(4) << best_ssw_d << "\n";
        } else {
            cout << L("  数值过大，使用科学计数法 = ", "  Value too large, scientific notation = ", lang)
                 << scientific << setprecision(4) << best_ssw_d << "\n";
        }
        cout << string(52, '=') << "\n";

    } catch (const exception& e) {
        cerr << "异常: " << e.what() << "\n";
    } catch (...) {
        cerr << "未知异常\n";
    }

    cin.get();
    return 0;
}