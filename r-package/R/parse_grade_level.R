# Copyright (C) 2022 by Higher Expectations for Racine County

#' Title
#'
#' @param .column input data like c("1", "02", " 03", "KG")
#' @param pad_chars a vector of characters to remove
#'
#' @return a text vector with stripped grade numbers
#' @export
#'
#' @examples
#' parse_grade_level(c(1:3, "04", " 05", "PK", "KG"))

parse_grade_level <- function(.column,
                              pad_chars = c("\\s", 0)) {
    ex <- stringr::str_c(pad_chars,
                         collapse = "")
    stringr::str_remove(.column,
                        glue::glue("^[{ex}]*"))
}
