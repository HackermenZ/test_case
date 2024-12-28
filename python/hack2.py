from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data to simulate package versions
packages = {
    'express': ['4.17.1', '4.17.0', '4.16.4'],
    'lodash': ['4.17.21', '4.17.20', '4.17.19']
}

@app.route('/versions/<package_name>', methods=['GET'])
def get_versions(package_name):
    # Check if the package exists
    if package_name in packages:
        return jsonify({
            'package': package_name,
            'versions': packages[package_name]
        }), 200
    else:
        return jsonify({'error': 'Package not found'}), 404

@app.route('/newVersion/<package_name>', methods=['POST'])
def add_version(package_name):
    if package_name not in packages:
        return jsonify({'error': 'Package not found'}), 404
    
    # Retrieve the new version from the request body
    new_version = request.json.get('version')
    if not new_version:
        return jsonify({'error': 'No version provided'}), 400
    
    # Add the new version if it's not already in the list
    if new_version not in packages[package_name]:
        packages[package_name].append(new_version)
        return jsonify({
            'message': f'Version {new_version} added to {package_name}',
            'versions': packages[package_name]
        }), 201
    else:
        return jsonify({'error': 'Version already exists'}), 409

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)