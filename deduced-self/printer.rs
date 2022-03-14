trait Printer {
    fn print_line(&self, message: &str) -> &Self {
        self._write(&format!("{message}\n"));
        return self;
    }

    fn _write(&self, message: &str);
}


struct StdoutPrinter {}

impl StdoutPrinter {
    fn print_fancy(&self, message: &str) -> &Self {
        return self.print_line(&format!("~~~ {message} ~~~"));
    }
}

impl Printer for StdoutPrinter {
    fn _write(&self, message: &str) {
        print!("{message}");
    }
}


fn main() {
    let printer = StdoutPrinter{};
    printer.print_line("hello world").print_fancy("Traits work!");
}
