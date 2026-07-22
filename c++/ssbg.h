#ifndef SSBG_00
#define SSBG_00

#include <string>
#include <vector>
#include <boost/multiprecision/cpp_dec_float.hpp>

using decimal_t = boost::multiprecision::number<boost::multiprecision::cpp_dec_float<100>>;

// 分组结果结构体（避免 std::tuple + boost 结构化绑定问题）
struct GroupResult {
    int index;
    std::vector<decimal_t> left;
    std::vector<decimal_t> right;
    decimal_t left_mean;
    decimal_t right_mean;
};

// 函数声明
bool choice_language();
std::string L(const std::string& cn, const std::string& en, bool lang);
std::vector<decimal_t> user_input(bool const lang);
std::vector<decimal_t> get_input(int const min_count, bool const lang);
std::vector<GroupResult> average_value(const std::vector<decimal_t>& data);

#endif