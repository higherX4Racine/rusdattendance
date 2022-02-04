# Copyright (C) 2022 by  Higher Expectations for Racine County
#' @importFrom magrittr %>%

attendance_columns <- list(
    School = readr::col_character(),
    Calendar = readr::col_character(),
    Grade = readr::col_character(),
    `Student Count` = readr::col_number(),
    `Student Last Name` = readr::col_skip(),
    `Student First Name` = readr::col_skip(),
    `Student Middle Initial` = readr::col_skip(),
    `Student Number` = readr::col_skip(),
    `Membership Days` = readr::col_number(),
    `Absent Days` = readr::col_number(),
    `Present Days` = readr::col_number(),
    ADM = readr::col_number(),
    ADA = readr::col_number(),
    `Unexcused Days` = readr::col_number(),
    `Absences avg. Daily` = readr::col_number(),
    `Percent In Attendance` = readr::col_number()
)

grade_levels <- c(
        "E3",
        "PK",
        "E4",
        "K4",
        "KG",
        1:12
    )

#' Read a CSV file with ADM and ADA attendance data
#'
#' @param file_name The location of the file
#'
#' @return a tibble
#' @export
read_adm_ada <- function(file_name) {
    readr::read_csv(file_name,
                    col_names = TRUE,
                    col_types = attendance_columns,
                    lazy = FALSE) %>%
        dplyr::filter(!is.na(Calendar) &
                          `Student Count` > 0 &
                          !stringr::str_detect(School,
                                               "Census|Summer|Extended")) %>%
        unique() %>%
        tidyr::extract(Calendar,
                       c("Calendar Year",
                         "Calendar School"),
                       "^(\\d+-\\d+) (.*)$") %>%
        dplyr::mutate(
            Year = stringr::str_extract(`Calendar Year`,
                                        "(.*)-") %>%
                readr::parse_number(),
            Grade = readr::parse_factor(parse_grade_level(Grade),
                                        levels = grade_levels),
            Tier = forcats::fct_collapse(Grade,
                                         Early = grade_levels[1:4],
                                         Elementary = grade_levels[5 + 0:5],
                                         Middle = grade_levels[5 + 6:8],
                                         High = grade_levels[5 + 9:12]
            )
        ) %>%
        invisible()
}
