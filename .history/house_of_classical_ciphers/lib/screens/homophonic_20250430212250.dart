import 'package:flutter/material.dart';
import 'dart:io';

class homophonic extends StatefulWidget {
  const Homophonic({super.key});

  @override
  State<Homophonic> createState() => _HomophonicState();
}

class _HomophonicState extends State<Homophonic> {
  final textController = TextEditingController();
  String result = '';

  Future<void> runHomophonic(String mode) async {
    final text = textController.text;

    List<String> arguments = ['python/python/homophonic.py', mode, text];

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
