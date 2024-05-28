#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
//Content Moderation in C++

bool containsSpam(const std::string& text, const std::vector<std::string>& keywords) {
  // Convert text to lowercase for case-insensitive matching
  std::string lowercaseText = text;
  std::transform(lowercaseText.begin(), lowercaseText.end(), lowercaseText.begin(), ::tolower);

  // Iterate through keywords and perform a case-insensitive search
  for (const std::string& keyword : keywords) {
    if (lowercaseText.find(keyword) != std::string::npos) {
      return true;
    }
  }
  return false;
}

int main() {
  // Define a list of spam keywords
  std::vector<std::string> keywords = {"spam", "free money", "click here"};

  // Test some content
  std::string content1 = "This is a normal message";
  std::string content2 = "Click here to win a free car!";

  // Check for spam
  if (containsSpam(content1, keywords)) {
    std::cout << content1 << " - Contains spam\n";
  } else {
    std::cout << content1 << " - Safe\n";
  }

  if (containsSpam(content2, keywords)) {
    std::cout << content2 << " - Contains spam\n";
  } else {
    std::cout << content2 << " - Safe\n";
  }

  return 0;
}