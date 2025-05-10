import 'package:flutter/material.dart';
import 'package:house_of_classical_ciphers/screens/AlbertiScreen.dart.dart';
import 'package:house_of_classical_ciphers/screens/atbashScreen.dart';
import 'package:house_of_classical_ciphers/screens/homophonicScreen.dart';


class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  final List<String> algorithms = const [
    'Atbash Cipher',
    'Homophonic Cipher',
    'Columnar Transposition Cipher',
    'Baconian Cipher',
    'Alberti Cipher',
    'Beaufort Cipher',
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('House of Classical Ciphers'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: ListView.builder(
          itemCount: algorithms.length,
          itemBuilder: (context, index) {
            return Padding(
              padding: const EdgeInsets.symmetric(vertical: 10),
              child: ElevatedButton(
                onPressed: () {
                  Widget destinationPage;

                  switch (algorithms[index]) {
                    case 'Atbash Cipher':
                      destinationPage = const AtbashPage();
                      break;
                    case 'Homophonic Cipher':
                      destinationPage = const HomophonicPage();
                      break;
                    case 'Columnar Transposition Cipher':
                      destinationPage = const Colum();
                      break;
                    case 'Baconian Cipher':
                      destinationPage = const AffinePage();
                      break;
                    case 'Alberti Cipher':
                      destinationPage = const RailFencePage();
                      break;
                    case 'Beaufort Cipher':
                      destinationPage = const MonoalphabeticPage();
                      break;
                    default:
                      destinationPage = const Scaffold(
                        body: Center(child: Text('Coming Soon')),
                      );
                  }

                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => destinationPage),
                  );
                },
                style: ElevatedButton.styleFrom(
                  minimumSize: const Size(double.infinity, 50),
                  textStyle: const TextStyle(fontSize: 18),
                ),
                child: Text(algorithms[index]),
              ),
            );
          },
        ),
      ),
    );
  }
}
