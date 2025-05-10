import 'package:flutter/material.dart';
import 'dart:io';

class HomophonicPage extends StatefulWidget {
  const HomophonicPage({super.key});

  @override
  State<HomophonicPage> createState() => _HomophonicPageState();
}

class _HomophonicPageState extends State<HomophonicPage> {
  final textController = TextEditingController();
  final keyController = TextEditingController();
  String result = '';

  Future<void> runHomophonic(String mode) async {
    final text = textController.text;
    final key = keyController.text;

    List<String> arguments = [];
    if (mode == "crack") {
      arguments = ['python/Homophonic.py', mode, text];
    } else {
      arguments = ['python/Homophonic.py', mode, text, key];
    }

    final process = await Process.run('python', arguments);
    setState(() {
      result = process.stdout.toString();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Homophonic Cipher')),
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
                  onPressed: () => runHomophonic("encrypt"),
                  child: const Text("Encrypt"),
                ),
                ElevatedButton(
                  onPressed: () => runHomophonic("decrypt"),
                  child: const Text("Decrypt"),
                ),
                ElevatedButton(
                  onPressed: () => runHomophonic("crack"),
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
