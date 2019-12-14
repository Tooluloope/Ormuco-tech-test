from compare_version import version

# Main method
if __name__ == '__main__':
    try:
        version1= input('Enter the first version \n')
        version2= input('Enter the second version \n')
        
        # Calling function version
        result = version(version1, version2)
        print(result)

    except ValueError:
        print('\n')
        print('_' * 42)
        print('Characters, strings are not allowed\n'
              "Please Enter only numbers \n{0}".format('_' * 42))
