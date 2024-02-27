def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if exitstatus == 0:  # Si no hay errores (exitstatus 0 significa que todas las pruebas pasaron)
        terminalreporter.write_line("¡Todas las pruebas pasaron correctamente!")
