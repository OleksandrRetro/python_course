*** Variables ***
${URL}              https://www.epam.com/
${BROWSER}          Chrome
${lang_prefix}      xpath://*[@id="wrapper"]/div[2]/div[1]/header/div/ul/li[2]/div/button/span/div
${header_links_locator}      xpath=//*[@id="wrapper"]/div[2]/div[1]/header/div/nav/ul/li
@{header_links_text_list}    Services    Industries  Insights    About   Careers
${about_locator}      xpath://*[@id="wrapper"]/div[2]/div[1]/header/div/nav/ul/li[4]
${expected_url}     https://www.epam.com/about
${search_button_locator}    //*[@id="wrapper"]/div[2]/div[1]/header/div/ul/li[3]/div/button
${search_input_locator}    //*[@id="new_form_search"]
${find_button_locator}     css:.header-search__submit-text
${results_count_locator}    //*[@id="main"]/div[1]/div/section/div[3]/div[4]/section/h2
${search_error}     '31 RESULTS FOR "PYTHON"' does not contain '10'
