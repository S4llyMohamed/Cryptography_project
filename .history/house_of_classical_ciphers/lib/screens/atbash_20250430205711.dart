import 'package:flutter/material.dart';
import 'dart:io';

class CaesarPage extends StatefulWidget {
  const CaesarPage({super.key});

  @override
  State<CaesarPage> createState() => _CaesarPageState();
}

class _CaesarPageState extends State<CaesarPage> {
  final textController = TextEditingController();
  final keyController = TextEditingController();
  String result = '';

  Future<void> runCaesar(String mode) async {
    final text = textController.text;
    final key = keyController.text;

    List<String> arguments = [];
    if (mode == "crack") {
      arguments = ['python/Caesar.py', mode, text];
    } else {
      arguments = ['python/Caesar.py', mode, text, key];
    }

    final process = await Process.run('python', arguments);
    setState(() {
      result = process.stdout.toString();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text(' Cipher')),
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
                  onPressed: () => runCaesar("encrypt"),
                  child: const Text("Encrypt"),
                ),
                ElevatedButton(
                  onPressed: () => runCaesar("decrypt"),
                  child: const Text("Decrypt"),
                ),
                ElevatedButton(
                  onPressed: () => runCaesar("crack"),
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
