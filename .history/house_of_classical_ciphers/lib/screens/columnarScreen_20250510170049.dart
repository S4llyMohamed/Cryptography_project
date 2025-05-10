import 'package:flutter/material.dart';
import 'dart:io';

class ColumnarPage extends StatefulWidget {
  const ColumnarPage({super.key});

  @override
  State<ColumnarPage> createState() => _ColumnarPageState();
}

class _CaesarPageState extends State<ColumnarPage> {
  final textController = TextEditingController();
  final keyController = TextEditingController();
  String result = '';

  Future<void> runColumnar(String mode) async {
    final text = textController.text;
    final key = keyController.text;

    List<String> arguments = [];
    if (mode == "crack") {
      arguments = ['python/Columnar Transposition.py', mode, text];
    } else {
      arguments = ['python/Columnar Transposition.py', mode, text, key];
    }

    final process = await Process.run('python', arguments);
    setState(() {
      result = process.stdout.toString();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Columnar Transposition Cipher')),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            TextField(
              controller: textController,
              decoration: const InputDecoration(labelText: 'Enter text'),
            ),
            TextField(
              controller: keyController,
              decoration: const InputDecoration(
                labelText: 'Enter key (number)',
              ),
              keyboardType: TextInputType.number,
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                ElevatedButton(
                  onPressed: () => runColumnar("encrypt"),
                  child: const Text("Encrypt"),
                ),
                ElevatedButton(
                  onPressed: () => runColumnar("decrypt"),
                  child: const Text("Decrypt"),
                ),
                ElevatedButton(
                  onPressed: () => runColumnar("crack"),
                  child: const Text("Crack"),
                ),
              ],
            ),
            const SizedBox(height: 30),
            const Text(
              'Result:',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            Expanded(
              child: SingleChildScrollView(child: SelectableText(result)),
            ),
          ],
        ),
      ),
    );
  }
}
