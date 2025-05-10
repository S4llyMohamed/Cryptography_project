 void _complete() {
    assert(_completed == null);
    _completed = true;
    _primaryCompleter.complete();