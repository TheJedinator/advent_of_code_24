use std::fs::File;
use std::io::{self, BufRead};

fn read_reports_from_file(filename: &str) -> io::Result<Vec<Vec<i32>>> {
    let mut reports = Vec::new();
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        let report: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse().expect("parse error"))
            .collect();
        reports.push(report);
    }

    Ok(reports)
}

fn report_is_safe(report: Vec<i32>) -> bool {
    // IS SAFE
    //The levels are either all increasing or all decreasing.
    //Any two adjacent levels differ by at least one and at most three.
    let mut is_safe = true;
    let mut last_val = 0;
    for i in 1..report.len() {
        if (report[i] - last_val) > 3 {
            is_safe = false;
            break;
        }
        last_val = report[i];
    }
    is_safe
}

fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Dec 2 AOC 2024 Day 2");
    // IS SAFE
    //The levels are either all increasing or all decreasing.
    //Any two adjacent levels differ by at least one and at most three.

    let filename = "input.txt";
    let mut num_safe_reports = 0;

    match read_reports_from_file(filename) {
        Ok(reports) => {
            for report in reports {
                if report_is_safe(report) {
                    num_safe_reports += 1;
                }
            }
        }
        Err(e) => println!("Error reading file: {}", e),
    }
    println!("Number of safe reports: {}", num_safe_reports);
}
// }
